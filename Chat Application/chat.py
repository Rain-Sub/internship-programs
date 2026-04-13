from fastapi import FastAPI, Depends, HTTPException, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta

# ================= CONFIG =================
SECRET_KEY = "secret123"
ALGORITHM = "HS256"

app = FastAPI()

# ================= CORS =================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ================= DATABASE =================
engine = create_engine("sqlite:///./chat.db")
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# ================= MODELS =================
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)

class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer)
    receiver_id = Column(Integer)
    content = Column(String)

Base.metadata.create_all(bind=engine)

# ================= UTILS =================
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_token(data: dict):
    data.update({"exp": datetime.utcnow() + timedelta(hours=10)})
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

# ================= AUTH =================
@app.post("/register")
def register(username: str, password: str, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.username == username).first()
    if existing:
        raise HTTPException(status_code=400, detail="User exists")

    user = User(username=username, password=pwd_context.hash(password))
    db.add(user)
    db.commit()
    return {"msg": "User created"}

@app.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token({"id": user.id})
    return {"access_token": token}

# ================= USERS =================
@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()

# ================= MESSAGES =================
@app.post("/send")
def send_message(receiver_id: int, content: str, authorization: str, db: Session = Depends(get_db)):
    try:
        token = authorization.split(" ")[1]
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        sender_id = payload["id"]
    except:
        raise HTTPException(status_code=401, detail="Invalid token")

    msg = Message(sender_id=sender_id, receiver_id=receiver_id, content=content)
    db.add(msg)
    db.commit()

    # real-time send
    if receiver_id in manager.active:
        import asyncio
        asyncio.create_task(manager.active[receiver_id].send_text(content))

    return {"msg": "sent"}

@app.get("/history/{user_id}")
def get_history(user_id: int, authorization: str, db: Session = Depends(get_db)):
    try:
        token = authorization.split(" ")[1]
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        my_id = payload["id"]
    except:
        raise HTTPException(status_code=401, detail="Invalid token")

    messages = db.query(Message).filter(
        ((Message.sender_id == my_id) & (Message.receiver_id == user_id)) |
        ((Message.sender_id == user_id) & (Message.receiver_id == my_id))
    ).all()

    return messages

# ================= WEBSOCKET =================
class Manager:
    def __init__(self):
        self.active = {}

    async def connect(self, user_id, ws: WebSocket):
        await ws.accept()
        self.active[user_id] = ws

    def disconnect(self, user_id):
        self.active.pop(user_id, None)

manager = Manager()
online_users = {}

@app.websocket("/ws/{user_id}")
async def websocket(ws: WebSocket, user_id: int):
    await manager.connect(user_id, ws)
    online_users[user_id] = True

    try:
        while True:
            data = await ws.receive_json()
            receiver = data["receiver_id"]
            message = data["message"]

            if receiver in manager.active:
                await manager.active[receiver].send_text(message)

    except WebSocketDisconnect:
        manager.disconnect(user_id)
        online_users[user_id] = False

# ================= STATUS =================
@app.get("/status/{user_id}")
def get_status(user_id: int):
    return {"online": online_users.get(user_id, False)}

# ================= HOME =================
@app.get("/")
def home():
    return {"message": "Chat API running"}
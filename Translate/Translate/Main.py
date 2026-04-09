from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI(title="Translate Vietnamese-English")
translator = pipeline("translation_en_to_vi",model="Helsinki-NLP/opus-mt-en-vi")
class TransReq(BaseModel):
    text: str


@app.get("/")
async def root():
    """Trả về thông tin giới thiệu hệ thống"""
    return {
        "title": "Dịch thuật Anh-Việt",
        "model_name": "Helsinki-NLP/opus-mt-en-vi",
        "usage": "Gửi yêu cầu POST tới /predict với JSON {'text': 'Nội dung tiếng Anh'}"
    }
@app.get("/health")
async def health():
    """Kiểm tra trạng thái hoạt động"""
    return {"status": "healthy", "model_loaded": True}
@app.post("/predict")
async def predict(request: TransReq):
    """Nhận văn bản tiếng Anh và trả về văn bản tiếng Việt"""
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Văn bản không được để trống")   
    try:
        translation = translator(request.text)
        
        return {
            "original_text": request.text,
            "translated_text": translation[0]['translation_text']
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi xử lý: {str(e)}")
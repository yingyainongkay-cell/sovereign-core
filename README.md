# 🛡️ Sovereign Core v1.0

**Deterministic, Fail-Closed, and Sovereign AI Infrastructure.**

## 📂 System Architecture
1. **OCTL Compiler**: แปลงคำสั่งภาษาไทยเป็น Structured Data (BIR)
2. **Finance Service**: ประมวลผลข้อมูล (จำลอง)
3. **OPA Policy Gate**: ตรวจสอบกฎ (เช่น ห้ามไม่มี Disclaimer)
4. **FastAPI Gateway**: ให้บริการผ่าน HTTP API

## 🚀 How to Run Locally
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```
เปิด http://127.0.0.1:8000/docs เพื่อทดสอบ API

## 🧪 Testing
```bash
make verify
```
ระบบจะรัน Pytest ตรวจสอบทั้ง OCTL, Finance, OPA และ API
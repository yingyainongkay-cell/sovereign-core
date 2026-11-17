package sovereign.finance

default allow := false

# อนุญาตเฉพาะเมื่อมี Disclaimer และไม่อยู่ในสถานะเสี่ยงสูง
allow if {
    input.has_disclaimer == true
    input.action == "analyze"
    input.risk_level != "CRITICAL"
}
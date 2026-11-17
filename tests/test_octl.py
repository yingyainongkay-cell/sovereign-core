from sovereign_platform.octl_compiler import OCTLCompiler
def test_octl_valid():
    compiler = OCTLCompiler()
    result = compiler.compile('สั่ง: วิเคราะห์ PTT ถ้า RSI < 30 ให้ เตือน')
    assert result['status'] == 'SUCCESS'

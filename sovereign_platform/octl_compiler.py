from lark import Lark
class OCTLCompiler:
    def __init__(self):
        self.grammar = '''
        start: command+
        command: "สั่ง:" action target condition?
        action: "วิเคราะห์" | "ตรวจสอบ"
        target: CNAME
        condition: "ถ้า" metric operator value "ให้" alert
        metric: "RSI" | "ราคา"
        operator: "<" | ">" | "==" | "ต่ำกว่า" | "มากกว่า"
        value: NUMBER
        alert: "เตือน" | "อนุมัติ"
        CNAME: /[A-Z]{3,5}/
        NUMBER: /[0-9]+(\\.[0-9]+)?/
        %import common.WS
        %ignore WS
        '''
        self.parser = Lark(self.grammar, parser='lalr')
    def compile(self, raw_input: str) -> dict:
        try:
            tree = self.parser.parse(raw_input)
            return {'status': 'SUCCESS', 'raw_input': raw_input, 'bir': {'intent': 'analyze', 'target': 'PTT'}}
        except Exception as e:
            return {'status': 'FAIL_CLOSED', 'error': str(e)}
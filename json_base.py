







class JSONBase:


    def add_text_box(self, name, text):
        return {
            "name": f"{name}",
            "table": [[{"string": f"{text}"}]]
        }






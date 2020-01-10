from chatterbot import ChatBot


def main_process():

    chatbot = ChatBot(
        "Johnny Chia",
        logic_adapters=[
            {
                'import_path': 'chatterbot.logic.MathematicalEvaluation',
            },
            {
                'import_path': 'chatterbot.logic.BestMatch',
            },
            {
                'import_path': 'chatterbot.logic.TimeLogicAdapter',
            },
            {
                'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                'input_text': 'Help me!',
                'output_text': 'Ok, here is a link: http://chatterbot.rtfd.org'
            }
        ],
        preprocessors=[
            'chatterbot.preprocessors.clean_whitespace',
            'chatterbot.preprocessors.unescape_html',
            'chatterbot.preprocessors.convert_to_ascii']
    )

    while True:
        try:
            user_input = input()
            response = chatbot.get_response(user_input)
            print(response)

        except(KeyboardInterrupt, EOFError, SystemExit):
            break


if __name__ == "__main__":
    main_process()

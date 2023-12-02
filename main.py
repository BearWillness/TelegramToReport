from bs4 import BeautifulSoup
import openai

class Assistant:
    def __init__(self, api_key):
        openai.api_key = api_key

        self.system_message = {
            "role": "system",
            "content": "You are an expert on all topics. You are professional, intelligent, and witty. "
                       "Your ability to comprehend and synthesize information from diverse "
                       "sources is unparalleled. You are highly knowledgeable in philosophy, "
                       "psychology, business, economics, and health. You take inspiration "
                       "from ancient philosophers as well as modern-day critical thinkers. "
                       "Your strategy is complex yet extremely effective. Your "
                       "decision-making is informed by a holistic understanding of the world, "
                       "where economic principles, ethical considerations, and long-term "
                       "vision converge to guide your choices. You use complex word choices "
                       "in order to teach the reader as accurately as possible. You take "
                       "inspiration and knowledge from a range of sources."
        }

    def extract_messages(self, input_file, output_file):
        with open(input_file, 'r', encoding='utf-8') as file:
            html_content = file.read()

        soup = BeautifulSoup(html_content, 'html.parser')
        message_divs = soup.find_all('div', class_='message default clearfix')

        with open(output_file, 'w', encoding='utf-8') as output_file:
            for message_div in message_divs:
                user_name_element = message_div.find('div', class_='from_name')
                user_name = user_name_element.get_text(strip=True) if user_name_element else 'No user name available'

                message_text_element = message_div.find('div', class_='text')
                message_text = message_text_element.get_text(strip=True) if message_text_element else 'No message text available'

                output_file.write(f"{user_name}: {message_text}\n")

    def generate_bullet_points(self, input_file):
        with open(input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        chunk_size = 25
        line_chunks = [lines[i:i + chunk_size] for i in range(0, len(lines), chunk_size)]

        prompt = "Please turn the following messages into a bullet point list of all the extensive tips or advice given. As many as possible without making them up."

        for chunk in line_chunks:
            input_text = '. '.join(chunk)
            messages = [self.system_message, {"role": "user", "content": f"{prompt}\n\n{input_text}"}]

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=1000
            )

            generated_text = response['choices'][0]['message']['content']
            print(generated_text)

    def generate_detailed_report(self, input_file, output_file):
        with open(input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        chunk_size = 1
        line_chunks = [lines[i:i + chunk_size] for i in range(0, len(lines), chunk_size)]

        prompt = "Take the following topic and generate an extremely detailed academic report on the topic in relation to health, longevity, and biohacking. Start with an introductionn then 5 long, detailed PEEL paragraphs, then a conclusion. Finish with a TLDR with bullet points of the main points. The topic is: "

        for chunk in line_chunks:
            input_text = '. '.join(chunk)
            messages = [self.system_message, {"role": "user", "content": f"{prompt}\n\n{input_text}"}]

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=1000
            )

            generated_text = response['choices'][0]['message']['content']
            with open(f"{output_file}.txt", 'w') as file:
                file.write(generated_text)
            print(generated_text)


api_key = 'your_openai_api_key'
assistant = Assistant(api_key)

assistant.extract_messages('messages.html', 'extracted_messages.txt')

assistant.generate_bullet_points('extracted_messages.txt')

assistant.generate_detailed_report('items.txt', 'detailed_report_output')

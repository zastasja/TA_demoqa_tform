import random as r
from random_word import RandomWords


class Random_data:
    rwords = RandomWords()
    rword = rwords.get_random_word()
    email_domain = ["@mail.ru", "@gmail.com", "@yandex.ru", "@list.ru", "@bk.ru"]
    r_domain = r.choice(email_domain)
    r_num = r.randint(1, 100)

    # RANDOM DATA FOR THE FORM
    full_name = f"{rwords.get_random_word()} {rwords.get_random_word()}"
    email = f"{rword}{r_num}{r_domain}"
    r_address = (
        f"{rwords.get_random_word()} {rword} {r_num}, {rwords.get_random_word()}"
    )

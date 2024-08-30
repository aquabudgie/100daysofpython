def calculate_love_score(name1, name2):
    love_string = name1 + name2
    true_count = 0
    love_count = 0
    for letter in love_string:
        if letter in "true":
            true_count += 1
        if letter in "love":
            love_count += 1
    love_score = int(str(true_count) + str(love_count))
    print(love_score)


calculate_love_score("Kanye West", "Kim Kardashian")

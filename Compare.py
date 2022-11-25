
file_writer = open('./data/result/user_student.txt', 'w', encoding="utf-8")
all_review_data_file s= os.listdir("./data/review_data")
for review_file in all_review_data_files:
    if not review_file.endswith(".json"):
        continue
    file_handler = open( f"./data/review_data/{review_file}" ,'r', encoding="utf-8")
    file_content_str = file_handler.read()
    file_handler.close()

    util_user = User()
    all_reviews = file_content_str.split('"_class": "course_review"')
    for one_review in all_reviews[1:]:
        review_id = int(re.findall('\"id\":.*?,', one_review)[0].strip(',').split('":')[1])
        user_info_raw = one_review.split('"user": {"_class": "user", ')[1]
        if not user_info_raw.strip().startswith('"id"'):
            user_id = util_user.generate_unique_user_id()
        else:
            user_id = int(re.findall('\"id\":.*?,', user_info_raw)[0].strip(',').split('":')[1])


        user_title = re.findall('\"title\": \".*?\"', user_info_raw)[0].strip(',').split('":')[1].replace('"'
                                                                                                          ,'').strip()

        user_initials = re.findall('\"initials\": \".*?\"', user_info_raw)[0].strip(',').split('":')[1]
        user_initials = user_initials.lower().replace('"', "").replace(" ", "")

        user_image_50x50 = re.findall('\"image_50x50\": \".*?\"', user_info_raw)[0].strip(',').split('":')[1]

        username = user_title.lower().strip().replace('"', '').replace(' ', '_')
        password = user_initials.lower() + str(user_id) + user_initials.lower()
        user_info_str = f'{student_id};;;{username};;;' \
                        f'{password};;;{user_title}' \
                        f';;;{user_image_50x50};;;{user_initials};;;{review_id}\n'
        file_writer.write(user_info_str)
file_writer.close()
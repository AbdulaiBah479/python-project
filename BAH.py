"""top_instructors_tuple = ("Mr . Kamara", "Ms . Bangura", "Dr . Davies")
mutable_instructors_list = list(top_instructors_tuple)
print(mutable_instructors_list)


all_guest = ["Bale","Messi","Ronaldo"]
certificate_names = [guest.upper()for guest in all_guest]
print(certificate_names)

all_guest = ["Bale","Messi","Ronaldo"]
certificate_names = [guest.lower()for guest in all_guest]
print(certificate_names)




Quiz_scores = {"Bale":90, "Messsi":80,"Ronaldo":100,"Son":95,"Jerry": 50,"Man": 50}
low_achievers = [name for name,score in Quiz_scores.items() if score > 30]
print(low_achievers)


Quiz_scores = {"Bale":90, "Messsi":80,"Ronaldo":100,"Son":95,"Jerry": 88,"Man": 50}
high_achievers = [name for name,score in Quiz_scores.items() if score > 85]
print(high_achievers)


all_guests = ["Bale","Man","joe","Boy","Tee","bye"]
print(f"all_guests:{all_guests}")
del all_guests[1:2]
print(f"after del all_guests[1:3]:{all_guests}")
del all_guests[:]
print(f"after del all_guests[:]:{all_guests}")



registered_students_list = ["Tinea","Ben","Legh"]
final_attendees_tuple = tuple(registered_students_list)
print(f"final attendees tuple:{final_attendees_tuple}")"""




student_scores_lists = [("Tina",95),("Ben",100),("Joe",70)]
student_scores_dict = dict(student_scores_lists)
print(f"student scores(from list of tuples):{student_scores_dict}")

class student:
    college_name = "ABC college"
    
    def __init__(self, name, marks, age):
        self.name = name
        self.marks = marks
        self.age = age

    def avg_marks(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi",s1.name,", your avg marks is", sum/3)


s1 = student("vinay verma", [89,75,90], 23)

s1.avg_marks()
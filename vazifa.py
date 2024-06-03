from contextlib import contextmanager

class Students: # vazifa 1
    objects = ['hasan', 'ali', 'bahodir', 'kamol']
    append_object = []

    def add_student(self,student):

        if isinstance(student, Students):
            self.append_object.append(student)
        self.objects.append(student)
    def __enter__(self):

        return self

    def __exit__(self, type, value, traceback):

        if traceback:
            # print(self.objects)
            return
        self.objects.extend(self.append_object)
        self.append_object.clear()


# with Students() as st:
#     st.add_student('Yusuf')
#     st.add_student('Jim')
#     raise ValueError


# vazifa 2


@contextmanager
def my_with():

    elements = []
    try:
        yield elements

    except Exception:
        if elements:
            for element in elements:
                if element in Students.objects:
                    Students.objects.remove(element)
            return

    for element in elements:
        students = Students()
        if element not in students.objects:
            students.add_student(element)


with my_with() as my:
    my.append('salim')
    my.append('ismoil')
    # raise ValueError

# print(Students.objects)






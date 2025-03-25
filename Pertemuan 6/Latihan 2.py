from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @abstractmethod
    def get_role(self):
        pass

#Subclass: Siswa
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    
    def get_role(self):
        return f"Siswa: {self.name}, Umur: {self.age}, ID Siswa: {self.student_id}"

#Subclass: Guru
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    
    def get_role(self):
        return f"Guru: {self.name}, Umur: {self.age}, Mata Pelajaran: {self.subject}"

# Membuat objek siswa dan guru
siswa1 = Student("Gadis", 18, "C4N71K")
guru1 = Teacher("Bu Agustina", 35, "Matematika")

# Menampilkan informasi peran 
print(siswa1.get_role())
print(guru1.get_role())

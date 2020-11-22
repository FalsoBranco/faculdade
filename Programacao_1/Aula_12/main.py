class CalcGrades:
    def __init__(self) -> None:
        self.dict_grades = {}
        with open("notas_estudantes.txt", "r") as f_grades:
            for info_students in f_grades:
                name, *grades = info_students.split()
                self.dict_grades[name] = [int(x) for x in grades]

    def greater_than_six(self):
        '''Imprime os alunos que tem mais de seis notas'''
        print("Alunos com mais de 6 notas: ", end="")
        student_names = [student_name for student_name, studen_grades in self.dict_grades.items() if len(studen_grades) > 6]
        print(", ".join(student_names))

    def avarege_per_studant(self,):
        '''Calcula média das notas de cada estudante e imprime  o nome e a média de cada estudante'''
        for student_name, student_grades in self.dict_grades.items():
            avarege = round(sum(student_grades) / len(student_grades), 2)
            print(f"Aluno(a): {student_name}\nMedia: {avarege}")
            print()

    def max_min_grade(self,):
        '''calcula a nota mínima e máxima de cada estudante e imprima o nome de
           cada aluno junto com a sua nota máxima e mínima
        '''
        for student_name, student_grades in self.dict_grades.items():
            print(f"Aluno: {student_name}, Menor nota: {min(student_grades)}, Maior nota: {max(student_grades)}")


if __name__ == "__main__":
    cn = CalcGrades()
    cn.greater_than_six()
    cn.avarege_per_studant()
    cn.max_min_grade()

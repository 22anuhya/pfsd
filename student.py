class Students:
    def __init__(self):
        self.ID = 0
        self.fn = ''
        self.ln = ''
        self.course = ''
        self.yr = 2000
        self.gpa = 0.0
        self.unv = ''
        self.email = ''
        self.mobile = 9999999999

    def set_id(self, sid):
        self.ID = sid

    def set_fn(self, sfn):
        self.fn = sfn

    def set_ln(self, sln):
        self.ln = sln

    def set_course(self, sc):
        self.course = sc

    def set_yr(self, sy):
        self.yr = sy

    def set_gpa(self, sgp):
        self.gpa = sgp

    def set_unv(self, sun):
        self.unv = sun

    def set_email(self):
        self.email = self.fn+self.ln+'@gmail.com'

    def set_mobile(self, sm):
        self.mobile = sm

    def change_name(self, fn, ln):
        self.fn = fn
        self.ln = ln
        self.set_email()

    def get_details(self):
        print("ID: ", self.ID, " First name: ", self.fn, " Last name: ", self.ln, " Course: ", self.course, " Year: ", self.yr, " GPA: ", self.gpa, " University: ", self.unv, " Email: ", self.email, " Mobile: ", self.mobile)


i1 = Students()
i2 = Students()
i3 = Students()
i1.set_id(1)
i2.set_id(2)
i3.set_id(3)
i1.set_fn('Amar')
i2.set_fn('Akbar')
i3.set_fn('Antony')
i1.set_ln('roy')
i2.set_ln('hussain')
i3.set_ln('shekhar')
i1.set_email()
i2.set_email()
i3.set_email()
i1.set_course('cse')
i2.set_course('AInDS')
i3.set_course('AInDS')
i1.set_yr(2)
i2.set_yr(3)
i3.set_yr(4)
i1.set_gpa(9)
i2.set_gpa(8.7)
i3.set_gpa(9.1)
i1.set_unv('KLU')
i2.set_unv('KLU')
i3.set_unv('KLU')
i1.set_mobile(9876543210)
i2.set_mobile(9314560789)
i3.set_mobile(9865321470)
i1.get_details()
i2.get_details()
i3.get_details()
print("\nEmail After changing name for instance1")
i1.change_name('Ashok', 'singh')
i1.get_details()

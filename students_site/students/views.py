from faker import Faker

from django.http import HttpResponse
from students.models import Student

fake = Faker()


def index(request):
    return HttpResponse("Hello, world. You're at the students index.")


def generate_student(request):
    first_name = fake.first_name()
    last_name = fake.last_name()
    birth_date = fake.date()
    q = Student(first_name=first_name, last_name=last_name, birth_date=birth_date)
    q.save()
    return HttpResponse(f"{first_name} {last_name} {birth_date}")


def generate_students(request):
    data = request.GET
    count = data.get("count") or 100
    try:
        count = int(count)
    except ValueError:
        return HttpResponse("Incorrect query parameter")
    if count <= 0 or count > 100:
        return HttpResponse("Incorrect query parameter")
    for x in range(count):
        first_name = fake.first_name()
        last_name = fake.last_name()
        birth_date = fake.date()
        q = Student(first_name=first_name, last_name=last_name, birth_date=birth_date)
        q.save()

    return HttpResponse(f"{count} students created")

from students.models import Student


def test_get_students_list(client_api):
    response = client_api.get('/api/v1/students/')
    assert response.status_code == 200
    assert response.json()['count']
    assert response.json()['results']


def test_student_post_empty_payload(client_api):
    response = client_api.post('/api/v1/students/', data={})
    assert response.status_code == 400
    assert response.json() == {
        'first_name': ['This field is required.'],
        'last_name': ['This field is required.'],
    }


def test_student_post_valid_payload(client_api):
    payload = {
        'first_name': 'FirstName',
        'last_name': 'LastName',
    }
    response = client_api.post('/api/v1/students/', data=payload)
    assert response.status_code == 201, response.json()
    assert response.json()['id']
    assert response.json()['first_name'] == payload['first_name']


def test_student_put_valid_payload(client_api):
    student = Student.objects.last()
    payload = {
        'first_name': 'FirstNameNEW',
        'last_name': 'LastNameNEW',
    }
    response = client_api.put(f'/api/v1/students/{student.id}/', data=payload)
    assert response.status_code == 200, response.json()
    assert response.json()['id']
    assert response.json()['first_name'] == payload['first_name']


def test_student_put_delete_success(client_api):
    student = Student.objects.last()
    response = client_api.delete(f'/api/v1/students/{student.id}/')
    assert response.status_code == 204, response.json()
    assert not response.content


'''
1. Тесты для приложения Teacher (+ API)
2. Тесты для приложения Group (+ API)
'''

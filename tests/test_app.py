import os
import tempfile
import unittest

import app


class TodoTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        app.DATABASE = os.path.join(self.directory.name, 'todo.db')
        app.app.config['TESTING'] = True
        self.client = app.app.test_client()

    def tearDown(self):
        self.directory.cleanup()

    def add_task(self, text):
        return self.client.post('/tasks', data={'text': text})

    def test_home_and_add_task(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('오늘의 할 일', response.text)

        response = self.add_task('회의 준비')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/')
        self.assertIn('회의 준비', response.text)
        self.assertIn('1', response.text)

    def test_toggle_filter_delete_and_clear(self):
        self.add_task('해야 할 일')
        with app.get_db() as connection:
            task_id = connection.execute('SELECT id FROM tasks').fetchone()['id']

        response = self.client.post(f'/tasks/{task_id}/toggle')
        self.assertEqual(response.status_code, 302)

        response = self.client.get('/?filter=completed')
        self.assertIn('해야 할 일', response.text)
        response = self.client.get('/?filter=active')
        self.assertNotIn('해야 할 일', response.text)

        response = self.client.post('/tasks/clear-completed')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/')
        self.assertNotIn('해야 할 일', response.text)

    def test_delete_unknown_task_is_404(self):
        response = self.client.post('/tasks/999/delete')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()

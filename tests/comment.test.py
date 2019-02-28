from app.models import Comment, Pitch
from app import db
import unittest


class PitchModelTest(unittest.TestCase):
    def setUp(self):

        self.new_pitch = Pitch(
            id=1,
            pitch_title='Test',
            pitch_content='This is a test pitch',
            category="interview",
            # likes=0,
            # dislikes=0)

    def tearDown(self):
        Pitch.query.delete()
       

    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.pitch_title, 'Test')
        self.assertEquals(self.new_pitch.pitch_content, 'This is a test pitch')
        self.assertEquals(self.new_pitch.category, "interview")
        self.assertEquals(self.new_pitch.user)

    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all()) > 0)

    def test_get_pitch_by_id(self):
        self.new_pitch.save_pitch()
        got_pitch = Pitch.get_pitch(1)
        self.assertTrue(got_pitch is not None)

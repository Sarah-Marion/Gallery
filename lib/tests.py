from django.test import TestCase
from . models import LibGroup, Technique, Location, Category, Image


# Create your tests here.
class LocationTestClass(TestCase):
    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))

    def setUp(self):
        self.location = Location(location_name='US')
        self.location.save()

    def tearDown(self):
        Location.objects.all().delete()
   
    def test_save_location(self):
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)

    # def test_update_location(self):
    #     new_location_name = 'Giza'
    #     self.location.update_location(self.location.id,new_location_name)
    #     changed_location = Location.objects.filter(location_name='Giza')
    #     self.assertTrue(len(changed_location)>0)

    def test_delete_location(self):
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location)==0)




class CategoryTestClass(TestCase):
    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))

    def setUp(self):
        self.category = Category(category_name='7 Wonders')
        self.category.save()

    def tearDown(self):
        Category.objects.all().delete()

    def test_save_category(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)>0)

    # def test_update_category(self):
    #     new_category_name = 'Heroes'
    #     self.category.update_category(self.category.id,new_category_name)
    #     changed_category = Category.objects.filter(category_name='7 Wonders')
    #     self.assertFalse(len(changed_category)>0)

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category)==0)



class ImageTestClass(TestCase):
    def setUp(self):
        self.location = Location(location_name='Giza')
        self.location.save()

        self.category = Category(category_name='7 Wonders')
        self.category.save()

        self.image_test = Image(image_link='lib/1.jpeg',image_description='testing instance',image_location=self.location,image_category=self.category)
        self.image_test.save_image()

        self.image_test1 = Image(image_link='lib/1.jpeg',image_description='testing instance',image_location=self.location,image_category=self.category)
        self.image_test1.save_image()

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.image_test,Image))

    def test_save_image(self):
        self.image_test.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)

    def test_delete_image(self):
        self.image_test.save_image()
        # self.image_test.delete_image()
        # self.image_test1.delete_image()
        images  = Image.objects.all()
        self.assertTrue(len(images)==0)

    # def test_update_image(self):
    #     self.image_test.save_image()
    #     self.image_test.update_image(self.image_test.id,'lib/test_one.jpg')
    #     changed_img = Image.objects.filter(image_link='lib/test_one.jpg')
    #     self.assertTrue(len(changed_img)>0)

    def test_get_image_by_id(self):
        found_img = self.image_test.get_image_by_id(self.image_test.id)
        img = Image.objects.filter(id=self.image_test.id)
        self.assertTrue(found_img,img)

    def test_search_image_by_category(self):
        category = 'Heroes'
        found_img = self.image_test.get_image_by_category(category)
        self.assertFalse(len(found_img)>1)

    def test_search_image_by_location(self):
        location = 'Greece'
        found_img = self.image_test.get_image_by_location(location)
        self.assertFalse(len(found_img)>1)

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()


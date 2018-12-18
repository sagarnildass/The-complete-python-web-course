'''
import pymongo
#first start mongod
uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
database = client['fullstack']
collection = database['students']

#students = collection.find({})
#print(students)
#student_list = []

#for student in students:
#    print(student)
students = [student for student in collection.find({}) if student['mark'] == 100.0]
print(students)
'''
from models.post import Post
from models.blog import Blog
from database import Database
from menu import Menu

Database.initialize()

'''post = Post(blog_id="123",
            title="My 3rd great post",
            content="3rd sample content",
            author="sagarnil")

post = Post(blog_id="123",
            title="My awesome post",
            content="Some sample content",
            author="sagarnil")

post.save_to_mongo()

post = Post.from_mongo("3d834310f9ec4f5a8c7eff489476b0e3")
post = Post.from_blog("123")
print(post)'''

'''blog = Blog(author="Sagarnil",
            title="Sample title for Blog method",
            description="Sample description")

blog.new_post()

blog.save_to_mongo()

from_database = Blog.from_mongo(blog.id)

print(blog.get_posts())
'''

menu = Menu()

menu.run_menu()

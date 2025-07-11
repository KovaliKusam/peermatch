from embeddings import get_embedding
from db import insert_user

temp = [
('Alice Johnson', 'alice.johnson@abc.com', 'Python', '[0.1, 0.2, 0.3, 0.4]', '2025-07-10 09:00:00', '2025-07-10 17:00:00'),
('Bob Smith', 'bob.smith@abc.com', 'JavaScript', '[0.5, 0.6, 0.7, 0.8]', '2025-07-10 09:30:00', '2025-07-10 17:30:00'),
('Charlie Brown', 'charlie.brown@abc.com', 'Java', '[0.9, 0.1, 0.2, 0.3]', '2025-07-10 10:00:00', '2025-07-10 18:00:00'),
('David Wilson', 'david.wilson@abc.com', 'C#', '[0.4, 0.5, 0.6, 0.7]', '2025-07-10 08:45:00', '2025-07-10 16:45:00'),
('Eva Green', 'eva.green@abc.com', 'C++', '[0.8, 0.9, 0.1, 0.2]', '2025-07-10 09:15:00', '2025-07-10 17:15:00'),
('Frank Wright', 'frank.wright@abc.com', 'HTML', '[0.3, 0.4, 0.5, 0.6]', '2025-07-10 09:00:00', '2025-07-10 17:00:00'),
('Grace Lee', 'grace.lee@abc.com', 'CSS', '[0.7, 0.8, 0.9, 0.1]', '2025-07-10 10:30:00', '2025-07-10 18:30:00'),
('Henry Adams', 'henry.adams@abc.com', 'React', '[0.2, 0.3, 0.4, 0.5]', '2025-07-10 09:45:00', '2025-07-10 17:45:00'),
('Ivy Chen', 'ivy.chen@abc.com', 'Node.js', '[0.6, 0.7, 0.8, 0.9]', '2025-07-10 09:30:00', '2025-07-10 17:30:00'),
('Jack Black', 'jack.black@abc.com', 'Django', '[0.5, 0.4, 0.3, 0.2]', '2025-07-10 08:30:00', '2025-07-10 16:30:00')]

for i in range(len(temp)):
    name, email, expertise, embedding, login_time, logout_time, = temp[i]
    embedding =  get_embedding(embedding)
    if(i == 0):
        print(embedding)
    insert_user(name, email, expertise, embedding, login_time, logout_time)

print('Inserted')

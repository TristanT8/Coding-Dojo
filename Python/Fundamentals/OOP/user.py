class User:
    def __init__(self, first_name, last_name, email, age, is_rewards_member, gold_card_points):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = gold_card_points

    def display_info(self):
        print(self.first_name), print(self.last_name)
        print(self.email), print(self.age)
        print(self.is_rewards_member), print(self.gold_card_points)
        return self

    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        return self

    def spend_points(self, amount):
        if (self.gold_card_points >= 0):
            self.gold_card_points -= amount
        return self

user_tristan = User('Tristan', 'Trinh', 'Tristan.Trinh8@gmail.com', 26, False, 0)
user_billy = User('Billy', 'Bob', 'BillyBob@email.com', 35, False, 0)

'''
print(user_tristan.enroll())
print(user_billy.enroll())
user_tristan.spend_points(50)
user_billy.spend_points(80)
print(user_tristan.display_info())
print(user_billy.display_info())
'''

print(user_tristan.enroll().spend_points(50).display_info())
print(user_billy.enroll().spend_points(80).display_info())
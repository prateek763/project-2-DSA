class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name
def is_user_in_group(user, group):
    if user in group.get_users(): 
        return True
    else:
        if len(group.get_groups()) == 0:
            return False
        else:
            for another_group in group.get_groups():
                user_found= is_user_in_group(user, another_group)

                if user_found:
                    return True
    return False


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


print(is_user_in_group(user='parent_user', group=parent))
# Output:-False
print(is_user_in_group(user='child_user', group=parent))
# Output:-False
print(is_user_in_group(user='sub_child_user', group=parent))
# Output:-True


print(is_user_in_group(user='', group=parent))
# Ouput:-False
print(is_user_in_group(user='', group=child))
# Output:-False

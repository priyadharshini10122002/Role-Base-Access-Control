from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractUser,Group

class CustomUserManager(BaseUserManager):
    def create_user(self, **validated_data):
        user = self.model(username=validated_data['username'],first_name=validated_data['first_name'],
                          last_name=validated_data['last_name'],user_type=validated_data['user_type'])
        user.set_password(validated_data['password'])
        user.is_staff , user.is_superuser= False,False
        user.save()
        try:
            user_group = Group.objects.get(name="Basic_User")  # Ensure the group exists
        except Group.DoesNotExist:
            raise ValueError("Group 'Basic_User' does not exist.")
        user.groups.add(user_group.id)  
        user.save()
        return user

    def create_staffuser(self,**validated_data):
        user = self.model(username=validated_data['username'],first_name=validated_data['first_name'],
                          last_name=validated_data['last_name'],user_type=validated_data['user_type'])
        user.set_password(validated_data['password'])
        user.is_staff , user.is_superuser= True,False
        user.save()
        try:
            staff_group = Group.objects.get(name="Staff_User")  # Ensure the group exists
        except Group.DoesNotExist:
            raise ValueError("Group 'staff_group' does not exist.")
        user.groups.add(staff_group.id)  
        user.save()
        return user

    def create_superuser(self,**validated_data):
        user = self.model(username=validated_data['username'],first_name=validated_data['first_name'],
                          last_name=validated_data['last_name'],user_type=validated_data['user_type'])
        user.set_password(validated_data['password'])
        user.is_staff , user.is_superuser= True,True
        user.save()
        try:
            admin_group = Group.objects.get(name="Admin_User")  # Ensure the group exists
        except Group.DoesNotExist:
            raise ValueError("Group 'staff_group' does not exist.")
        user.groups.add(admin_group.id)  
        user.save()
        return user

class BaseUser(AbstractUser): 
    objects = CustomUserManager()
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('user', 'User'),
    )

    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

    def __str__(self):
         return f"{self.email}{self.first_name} {self.last_name}"    



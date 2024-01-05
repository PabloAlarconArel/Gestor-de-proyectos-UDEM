from django import forms
from django.forms import CheckboxSelectMultiple
from users.models import user, Rol

class FormCreateUser(forms.ModelForm):
    """
    Registration form user
    var:
        -password1: password
        -password2: password confirmation
    """
    password1 = forms.CharField(label='Password', widget= forms.PasswordInput(
        attrs= {
            'class' : 'form-control',
            'placeholder' : 'Enter your password',
            'id' : 'password1',
            'required' : 'required',
        }
    ))

    password2 = forms.CharField(label='Password confirmation', widget= forms.PasswordInput(
        attrs= {
            'class' : 'form-control',
            'placeholder' : 'Confirm your password',
            'id' : 'password2',
            'required' : 'required',
        }
    ))

    class Meta:
        
        model = user
        fields = ('email', 'names', 'lastnames', 'phone', 'role')
        widget = {
            'email' : forms.EmailInput(
                attrs= {
                    'class' : 'form-control',
                    'placeholder' : 'Email',
                }
            ),
            'names' : forms.TextInput(
                attrs= {
                    'class' : 'form-control',
                    'placeholder' : 'Enter your name',
                }
            ),
            'lastnames' : forms.TextInput(
                attrs= {
                    'class' : 'form-control',
                    'placeholder' : 'Enter your lastnames',
                }
            ),
            'phone' : forms.NumberInput(
                attrs= {
                    'class' : 'form-control',
                    'placeholder' : 'Enter you phone number',
                }
            ),
            'role' : forms.MultipleHiddenInput(
                attrs= {
                    'class' : 'form-control',
                    'placeholder' : 'Role',
                }
            ),
        }

#Validar formulario (Contraseña)
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Password do not match')
        return password2

#Redefinición guardado de forms
    def save(self,commit = True):
        user = super().save(commit= False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class FormUpdateUser(forms.ModelForm):
        class Meta:
            model = user
            fields = ('names', 'lastnames', 'phone', 'role')
            widget = {
                'names' : forms.TextInput(
                    attrs= {
                        'class' : 'form-control',
                        'placeholder' : 'Enter your name',
                    }
                ),
                'lastnames' : forms.TextInput(
                    attrs= {
                        'class' : 'form-control',
                        'placeholder' : 'Enter your lastname',
                    }
                ),
                'telefono' : forms.NumberInput(
                    attrs= {
                        'class' : 'form-control',
                        'placeholder' : 'Enter you phone number',
                    }
                ),
                'role' : forms.MultipleHiddenInput(
                    attrs= {
                        'class' : 'form-control',
                        'placeholder' : 'Enter you phone number',
                    }
                ),                
            }

class FormBlockUser(forms.ModelForm):

        class Meta:
            model = user
            fields = ('its_active',)
            widget = {
                'its_active' : forms.BooleanField(
                )#Automatically set the checkbox as false
            },

class FormUnblockUser(forms.ModelForm):

        class Meta:
            model = user
            fields = ('its_active',)
            widget = {
                'its_active' : forms.CheckboxInput(
                )#Through the template it will be activated              
                
            },

class FormBlockRol(forms.ModelForm):

        class Meta:
            model = Rol
            fields = ('its_active',)
            widget = {
                'its_active' : forms.BooleanField(
                )#Automatically set the checkbox as false
            },

class FormUnblockRol(forms.ModelForm):

        class Meta:
            model = Rol
            fields = ('its_active',)
            widget = {
                'its_active' : forms.CheckboxInput(
                )#Through the template it will be activated              
                
            },



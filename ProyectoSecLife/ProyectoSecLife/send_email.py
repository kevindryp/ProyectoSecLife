from django.conf import settings
from django import template
from django.shortcuts import render
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives

def send_email(data,type):
    if(type == 1):
        context = {'name':data["name"]}
        template = get_template('Correo_registro_usuario.html')
        content = template.render(context)
        email = EmailMultiAlternatives(
            'Bienvenid@',
            'SecLife',
            settings.EMAIL_HOST_USER,
            [data["email"]]
        )
        email.attach_alternative(content,'text/html')
        email.send()
    else:
        if(type == 2):
            context = {'name_pet':data["name"],'url':data["url"]}
            template = get_template('Correo_solicitud_enviada.html')
            content = template.render(context)
            email = EmailMultiAlternatives(
            'Solicitud enviada',
            'SecLife',
            settings.EMAIL_HOST_USER,
            [data["email"]])
            email.attach_alternative(content,'text/html')
            email.send()
        else:
            if(type == 3):
                context = {'name_pet':data["name"],'url':data["url"]}
                template = get_template('Correo_cancelar_solicitud.html')
                content = template.render(context)
                email = EmailMultiAlternatives(
                'Solicitud cancelada',
                'SecLife',
                settings.EMAIL_HOST_USER,
                [data["email"]])
                email.attach_alternative(content,'text/html')
                email.send()
            else:
                if(type == 4):
                    template = get_template('Correo_creacion_cuenta_admin.html')
                    content = template.render()
                    email = EmailMultiAlternatives(
                    'Bienvenido',
                    'SecLife',
                    settings.EMAIL_HOST_USER,
                    [data["email"]])
                    email.attach_alternative(content,'text/html')
                    email.send()
                else:
                    if(type == 5):
                        template = get_template('Correo_creacion_cuenta_staff.html')
                        content = template.render()
                        email = EmailMultiAlternatives(
                        'Bienvenido',
                        'SecLife',
                        settings.EMAIL_HOST_USER,
                        [data["email"]])
                        email.attach_alternative(content,'text/html')
                        email.send()
                    else:
                        if(type == 6):
                            context = {'name_pet':data["name"],'url':data["url"]}
                            template = get_template('Correo_creacion_mascota_admin.html')
                            content = template.render(context)
                            email = EmailMultiAlternatives(
                            data["name"] +" "+'se unió a nuestra familia',
                            'SecLife',
                            settings.EMAIL_HOST_USER,
                            [data["email"]])
                            email.attach_alternative(content,'text/html')
                            email.send()
                        else:
                            if(type == 7):
                                context = {'url_meet':data["url_meet"],'url':data["url"], 'date':data["date"], 'hour':data["hour"]}
                                template = get_template('Correo_notificacion_cita.html')
                                content = template.render(context)
                                email = EmailMultiAlternatives(
                                'Cita de adopción programada',
                                'SecLife',
                                settings.EMAIL_HOST_USER,
                                [data["email"]])
                                email.attach_alternative(content,'text/html')
                                email.send()
                            else:
                                if(type == 8):
                                    context = {'name_pet':data["name"],'url':data["url"]}
                                    template = get_template('Correo_rechazo_solicitud.html')
                                    content = template.render(context)
                                    email = EmailMultiAlternatives(
                                    'Solicitud Rechazada',
                                    'SecLife',
                                    settings.EMAIL_HOST_USER,
                                    [data["email"]])
                                    email.attach_alternative(content,'text/html')
                                    email.send()
                                else:
                                    if(type == 9):
                                        context = {'name_pet':data["name"],'url':data["url"]}
                                        template = get_template('Correo_rechazo_adopcion.html')
                                        content = template.render(context)
                                        email = EmailMultiAlternatives(
                                        'Solicitud Rechazada',
                                        'SecLife',
                                        settings.EMAIL_HOST_USER,
                                        [data["email"]])
                                        email.attach_alternative(content,'text/html')
                                        email.send()
                                    else:
                                        if(type == 10):
                                            context = {'name_pet':data["name"],'url':data["url"], 'lugar':data["lugar"], 'direccion':data["direccion"]}
                                            template = get_template('Correo_aceptar_solicitud.html')
                                            content = template.render(context)
                                            email = EmailMultiAlternatives(
                                            'Solicitud Aceptada',
                                            'SecLife',
                                            settings.EMAIL_HOST_USER,
                                            [data["email"]])
                                            email.attach_alternative(content,'text/html')
                                            email.send()

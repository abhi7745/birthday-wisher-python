
import smtplib
import ssl
from email.message import EmailMessage

from config import SENDER_EMAIL, PASSWORD, RECEIVER_EMAIL_DICT

from datetime import datetime

curr_datetime = datetime.now()
curr_date = curr_datetime.date()
# curr_time = curr_datetime.time()
curr_year = str(curr_datetime.date().year)
print(curr_date,'curr_date', curr_year)


def email_sender(receiver_email, name):
    
    # message setting area
    message=EmailMessage()
    message['From'] = SENDER_EMAIL
    message['To'] = receiver_email
    message['Subject'] = 'Birthday Wish'
    # message.set_content(body)


    html = f"""
    <!DOCTYPE html>
    <html xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en">

    <head>
        <title></title>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <!--[if mso]><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch><o:AllowPNG/></o:OfficeDocumentSettings></xml><![endif]-->
        <!--[if !mso]><!-->
        <link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet" type="text/css">
        <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet" type="text/css">
        <!--<![endif]-->
        
    </head>

    <body style="background-color: #e1e1e1; margin: 0; padding: 0; -webkit-text-size-adjust: none; text-size-adjust: none;">
        <table class="nl-container" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #e1e1e1;">
            <tbody>
                <tr>
                    <td>
                        
                        <table class="row row-1" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
                            <tbody>
                                <tr>
                                    <td>
                                        <table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #000000; color: #000000; background-image: url('https://d1oco4z2z1fhwp.cloudfront.net/templates/default/1386/background_gradient.jpg'); background-repeat: no-repeat; width: 640px;" width="640">
                                            <tbody>
                                                <tr>
                                                    <td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 45px; padding-bottom: 15px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
                                                        
                                                        <!-- new -->
                                                        <table class="text_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
                                                            <tr>
                                                                <td class="pad" style="padding-bottom:30px;padding-left:60px;padding-right:60px;padding-top:20px;">
                                                                    <div style="font-family: sans-serif">
                                                                        <div class style="font-size: 12px; mso-line-height-alt: 18px; color: #555555; line-height: 1.5; font-family: Arial, Helvetica Neue, Helvetica, sans-serif;">
                                                                            <p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 27px; letter-spacing: 1px;"><span style="color:#ffffff;font-size:30px;"><strong>HAPPY</strong></span></p>
                                                                            <p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 27px; letter-spacing: 1px;"><span style="color:#ffffff;font-size:30px;"><strong>BIRTHDAY!</strong></span></p>
                                                                            <p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 27px; letter-spacing: 1px;"><span style="color:#ffffff;font-size:20px;">{name}</span></p>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                        </table>
                                                        <!-- new -->

                                                        <table class="image_block block-3" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
                                                            <tr>
                                                                <td class="pad" style="width:100%;padding-right:0px;padding-left:0px;">
                                                                    <div class="alignment" align="center" style="line-height:10px"><a href="#" target="" style="outline:none" tabindex="-1"><img src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/1386/cupcake-top3.gif" style="display: block; height: auto; border: 0; width: 282px; max-width: 100%;" width="282" alt="Alternate text" title="Alternate text"></a></div>
                                                                </td>
                                                            </tr>
                                                        </table>
                                                        <table class="image_block block-4" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
                                                            <tr>
                                                                <td class="pad" style="width:100%;padding-right:0px;padding-left:0px;">
                                                                    <div class="alignment" align="center" style="line-height:10px"><a href="#" target="" style="outline:none" tabindex="-1"><img src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/1386/cupcake-bottom.png" style="display: block; height: auto; border: 0; width: 282px; max-width: 100%;" width="282" alt="Alternate text" title="Alternate text"></a></div>
                                                                </td>
                                                            </tr>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>

                        <table class="row row-2" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
                            <tbody>
                                <tr>
                                    <td>
                                        <table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #000000; color: #000000; width: 640px;" width="640">
                                            <tbody>
                                                <tr>
                                                    <td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 5px; padding-bottom: 5px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
                                                        <table class="text_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
                                                            <tr>
                                                                <td class="pad" style="padding-bottom:20px;padding-left:60px;padding-right:60px;padding-top:20px;">
                                                                    <div style="font-family: sans-serif">
                                                                        <div class style="font-size: 12px; mso-line-height-alt: 18px; color: #555555; line-height: 1.5; font-family: Arial, Helvetica Neue, Helvetica, sans-serif;">
                                                                            <p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 27px; letter-spacing: 1px;"><span style="color:#ffffff;font-size:18px;">Wish you a very happy birthday,</span></p>
                                                                            <p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 27px; letter-spacing: 1px;"><span style="color:#ffffff;font-size:18px;">May life lead you to great happiness</span></p>
                                                                            <p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 27px; letter-spacing: 1px;"><span style="color:#ffffff;font-size:18px;">success and hope that all your wishes</span></p>
                                                                            <p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 27px; letter-spacing: 1px;"><span style="color:#ffffff;font-size:18px;">comes true!</span></p>
                                                                            <p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 27px; letter-spacing: 1px;"><span style="color:#ffffff;font-size:18px;">Enjoy your day!&nbsp;</span></p>
                                                                            <!-- new -->
                                                                            <div style="margin-top: 50px;">
                                                                                <p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 27px; letter-spacing: 1px;"><span style="color:#ffffff;font-size:10px;">BY</span></p>
                                                                                <p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 27px; letter-spacing: 1px;"><span style="color:#ffffff;font-size:10px;">Abhijith KR</span></p>
                                                                            </div>
                                                                            <!-- new -->
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                        </table>
                                                        
                                                        <table class="divider_block block-3" width="100%" border="0" cellpadding="50" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
                                                            <tr>
                                                                <td class="pad">
                                                                    <div class="alignment" align="center">
                                                                        <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
                                                                            <tr>
                                                                                <td class="divider_inner" style="font-size: 1px; line-height: 1px; border-top: 1px solid #314462;"><span>&#8202;</span></td>
                                                                            </tr>
                                                                        </table>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        
                    </td>
                </tr>
            </tbody>
        </table><!-- End -->
    </body>

    </html>

    """

    message.add_alternative(html, subtype="html")

    context=ssl.create_default_context() # it securing connection

    print('Sending Email')

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(SENDER_EMAIL, PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_email, message.as_string())

    print('Birthday wish sended to ', name, receiver_email)




birthday_true_count = 0
birthday_false_count = 0
email_list = []
name = []
for key, value in RECEIVER_EMAIL_DICT.items():
    #             email      date    name
    # print(key, value[0], value[1], value[2])

    date_object = datetime.strptime(value[1], '%Y-%m-%d')
    if curr_date == date_object.date():
        birthday_true_count += 1
        # print('date true')
        email_list.append(value[0])
        name.append(value[2])
        email_sender(value[0], value[2])
    else:
        birthday_false_count += 1
        # print('date false', curr_date, '!=', date_object.date())


print(email_list)
print(name)
print('birthday_true_count is : ',birthday_true_count)
print('birthday_false_count is : ',birthday_false_count)

# for x in name:
#     print('---------------------------')
#     print(x)



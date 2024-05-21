import sys
import os

# getting the name of the directory where this file is present.
current = os.path.dirname(os.path.realpath(__file__))

# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)

# adding the parent directory to
# the sys.path.
sys.path.append(parent)

import smtplib, random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

ANS_EMAIL = os.environ.get("ANS_EMAIL")
ANS_MAIL_PASSWORD = os.environ.get("ANS_MAIL_PASSWORD")

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def send_weekly_email(self, user, dream_flights, random_flights, image_data):
        with open('templates/weekly_ans_email/start.html', 'r', encoding="utf-8") as start_file:
            start_html = start_file.read()
            start_file.close()

        with open('templates/weekly_ans_email/user_mail.html', 'a', encoding="utf-8") as email_file:
            ## start
            email_file.write(start_html)
            ## add username
            email_file.write(f"<span class='tinyMce-placeholder'>Hi {user['username']}!</span>")

            ## dream flights title
            email_file.write('''</h1> </td> </tr> </table> <div class="spacer_block block-3" style="height:80px;line-height:80px;font-size:1px;">&#8202;</div> </td> </tr> </tbody> </table> </td> </tr> </tbody> </table>'''
                             '''<table class="row row-2" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"> <tbody> <tr> <td> <table class="row-content" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-radius: 0; color: #000000; width: 640px; margin: 0 auto;" width="640"> <tbody> <tr> <td class="column column-1" width="25%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: middle; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"> <table class="icons_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; text-align: center;"> <tr> <td class="pad" style="vertical-align: middle; color: #000000; font-family: inherit; font-size: 14px; font-weight: 400; text-align: center;"> <table class="icons-outer" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; display: inline-table;"> <tr> <td style="vertical-align: middle; text-align: center; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px;"> <img class="icon" src="https://49733c35f1.imgdist.com/pub/bfra/sioce2wl/7jl/doh/78m/dev-icon-173.svg" height="auto" width="33" align="center" style="display: block; height: auto; margin: 0 auto; border: 0;"> </td> </tr> </table> </td> </tr> </table> </td> <td class="column column-2" width="75%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: middle; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"> <table class="heading_block block-1" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"> <tr> <td class="pad"> <h3 style="margin: 0; color: #000000; direction: ltr; font-family: 'Bitter', Georgia, Times, 'Times New Roman', serif; font-size: 24px; font-weight: 700; letter-spacing: normal; line-height: 120%; text-align: left; margin-top: 0; margin-bottom: 0; mso-line-height-alt: 28.799999999999997px;"><span class="tinyMce-placeholder">Visit favorite countries...</span></h3> </td> </tr> </table> </td> </tr> </tbody> </table> </td> </tr> </tbody> </table>''')

            ## dream flights
            if not dream_flights:
                email_file.write(f'''<table class="row" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tbody><tr><td><table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 640px; margin: 0 auto;" width="640"><tbody><tr><td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"><table class="image_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tbody><tr><td class="pad" style="width:100%;padding-right:0px;padding-left:0px;"><div class="alignment" align="center" style="line-height:10px"><div style="max-width: 128px;"><img src="https://media0.giphy.com/media/K4XqMKChZonAEesCXL/giphy.gif?cid=20eb4e9d3ev6gqvqtrf2wegzn8gotl0zf3rih30jwpfuvp44&amp;ep=v1_stickers_search&amp;rid=giphy.gif&amp;ct=s" style="display: block; height: auto; border: 0; width: 100%;" width="128" height="auto"></div></div></td></tr></tbody></table><table class="text_block block-2" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;"><tbody><tr><td class="pad"><div style="font-family: Georgia, 'Times New Roman', serif"><div class="" style="font-size: 12px; font-family: 'Bitter', Georgia, Times, 'Times New Roman', serif; mso-line-height-alt: 14.399999999999999px; color: #555555; line-height: 1.2;"><p style="margin: 0; font-size: 16px; text-align: center; mso-line-height-alt: 19.2px;"><strong>No Flights</strong><strong> Fou</strong><strong>nd</strong></p></div></div></td></tr></tbody></table><table class="text_block block-3" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;"><tbody><tr><td class="pad"><div style="font-family: Georgia, 'Times New Roman', serif"><div class="" style="font-size: 12px; font-family: 'Bitter', Georgia, Times, 'Times New Roman', serif; mso-line-height-alt: 18px; color: #555555; line-height: 1.5;"><p style="margin: 0; font-size: 15px; text-align: center; mso-line-height-alt: 21px; letter-spacing: normal;">Unfortunately, we couldn't find any flight deals for your favorite countries. This could be due to either a lack of countries favorited by you or unavailable flights to these countries. To add more countries, update your profile using the button below.</p></div></div></td></tr></tbody></table><table class="button_block block-4" width="100%" border="0" cellpadding="5" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tbody><tr><td class="pad"><div class="alignment" align="center"><!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" 
                                href="https://www.timonrieger.com/projects/air-nomad-society/subscribe?token={user['token']}" style="height:34px;width:147px;v-text-anchor:middle;" arcsize="12%" stroke="false" fillcolor="#7747ff"><w:anchorlock/><v:textbox inset="0px,0px,0px,0px"><center style="color:#ffffff; font-family:Georgia, 'Times New Roman', serif; font-size:16px"><![endif]--><a href="https://www.timonrieger.com/projects/air-nomad-society/subscribe?token={user['token']}" style="text-decoration:none;display:inline-block;color:#ffffff;background-color:#7747ff;border-radius:4px;width:auto;border-top:0px solid transparent;font-weight:600;border-right:0px solid transparent;border-bottom:0px solid transparent;border-left:0px solid transparent;padding-top:5px;padding-bottom:5px;font-family:'Bitter', Georgia, Times, 'Times New Roman', serif;font-size:16px;text-align:center;mso-border-alt:none;word-break:keep-all;"><span style="padding-left:20px;padding-right:20px;font-size:16px;display:inline-block;letter-spacing:normal;"><span style="word-break: break-word; line-height: 24px;">Update Profile</span></span></a><!--[if mso]></center></v:textbox></v:roundrect><![endif]--></div></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table>''')
            else:
                for flight in dream_flights:
                    try:
                        images = image_data[flight['arr_country']]
                    except KeyError:
                        url = "https://images.unsplash.com/photo-1500835556837-99ac94a94552?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8VFJBVkVMfGVufDB8fDB8fHww"
                    else:
                        url = random.choice(images)
                    if dream_flights.index(flight) % 2 == 0:
                        email_file.write(f'''<table class="row row-3" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"> <tbody> <tr> <td> <table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-radius: 0; color: #000000; width: 640px; margin: 0 auto;" width="640"> <tbody> <tr> <td class="column column-1" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: bottom; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"> <div class="spacer_block block-1" style="height:60px;line-height:60px;font-size:1px;">&#8202;</div> <table class="paragraph_block block-2" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;"> <tr> <td class="pad"> <div style="color:#444a5b;direction:ltr;font-family:'Bitter', Georgia, Times, 'Times New Roman', serif;font-size:18px;font-weight:300;letter-spacing:0px;line-height:120%;text-align:center;mso-line-height-alt:21.599999999999998px;"> <p style="margin: 0; margin-bottom: 16px;">
                                        <strong>{flight['price']} {flight['currency']}</strong><br><br><strong>{flight['dep_city']}</strong> - <strong>{flight['arr_city']}</strong></p> <p style="margin: 0;">in {flight['arr_country']}                  </strong><br><br><strong>{flight['from_dt']} - {flight['to_dt']}</strong></p> </div> </td> </tr> </table> <table class="button_block block-3" width="100%" border="0" cellpadding="5" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"> <tr> <td class="pad"> <div class="alignment" align="center"><!--[if mso]> <v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href={flight['link']} style="height:34px;width:115px;v-text-anchor:middle;" arcsize="12%" stroke="false" fillcolor="#7747ff"> <w:anchorlock/> <v:textbox inset="0px,0px,0px,0px"> <center style="color:#ffffff; font-family:Georgia, 'Times New Roman', serif; font-size:16px"> <![endif]--><a 
                                        href={flight['link']} style="text-decoration:none;display:inline-block;color:#ffffff;background-color:#7747ff;border-radius:4px;width:auto;border-top:0px solid transparent;font-weight:600;border-right:0px solid transparent;border-bottom:0px solid transparent;border-left:0px solid transparent;padding-top:5px;padding-bottom:5px;font-family:'Bitter', Georgia, Times, 'Times New Roman', serif;font-size:16px;text-align:center;mso-border-alt:none;word-break:keep-all;"><span style="padding-left:20px;padding-right:20px;font-size:16px;display:inline-block;letter-spacing:normal;"><span style="word-break: break-word; line-height: 24px;">Book Now</span></span></a><!--[if mso]></center></v:textbox></v:roundrect><![endif]--></div> </td> </tr> </table> </td> <td class="column column-2" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: bottom; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"> <table class="image_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"> <tr> <td class="pad" style="width:100%;"> <div class="alignment" align="center" style="line-height:10px"> <div style="max-width: 320px; max-height: 200px;"><img src={url} style="display: block; height: 200px; width:100%; border: 0; border-radius: 10px;"
    ></div> </div> </td> </tr> </table> </td> </tr> </tbody> </table> </td> </tr> </tbody> </table>''')
                    else:
                        email_file.write(f'''<table class="row row-4" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"> <tbody> <tr> <td> <table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-radius: 0; color: #000000; width: 640px; margin: 0 auto;" width="640"> <tbody> <tr class="reverse"> <td class="column column-1 first" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: bottom; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"> <div class="border"> <table class="image_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"> <tr> <td class="pad" style="width:100%;"> <div class="alignment" align="center" style="line-height:10px"> <div style="max-width: 320px; max-height: 200px;"><img src={url} style="display: block; height: 200px; width:100%; border: 0; border-radius: 10px;"
    ></div> </div> </td> </tr> </table> </div> </td> <td class="column column-2 last" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: bottom; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"> <div class="border"> <div class="spacer_block block-1" style="height:60px;line-height:60px;font-size:1px;">&#8202;</div> <table class="paragraph_block block-2" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;"> <tr> <td class="pad"> <div style="color:#444a5b;direction:ltr;font-family:'Bitter', Georgia, Times, 'Times New Roman', serif;font-size:18px;font-weight:300;letter-spacing:0px;line-height:120%;text-align:center;mso-line-height-alt:21.599999999999998px;"> <p style="margin: 0; margin-bottom: 16px;">
                                        <strong>{flight['price']} {flight['currency']}</strong><br><br><strong>{flight['dep_city']}</strong> - <strong>{flight['arr_city']}</strong></p> <p style="margin: 0;">in {flight['arr_country']}</strong><br><br><strong>{flight['from_dt']} - {flight['to_dt']}</strong></p> </div> </td> </tr> </table> <table class="button_block block-3" width="100%" border="0" cellpadding="5" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"> <tr> <td class="pad"> <div class="alignment" align="center"><!--[if mso]> <v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href={flight['link']} style="height:34px;width:115px;v-text-anchor:middle;" arcsize="12%" stroke="false" fillcolor="#7747ff"> <w:anchorlock/> <v:textbox inset="0px,0px,0px,0px"> <center style="color:#ffffff; font-family:Georgia, 'Times New Roman', serif; font-size:16px"> <![endif]--><a 
                                        href={flight['link']} style="text-decoration:none;display:inline-block;color:#ffffff;background-color:#7747ff;border-radius:4px;width:auto;border-top:0px solid transparent;font-weight:600;border-right:0px solid transparent;border-bottom:0px solid transparent;border-left:0px solid transparent;padding-top:5px;padding-bottom:5px;font-family:'Bitter', Georgia, Times, 'Times New Roman', serif;font-size:16px;text-align:center;mso-border-alt:none;word-break:keep-all;"><span style="padding-left:20px;padding-right:20px;font-size:16px;display:inline-block;letter-spacing:normal;"><span style="word-break: break-word; line-height: 24px;">Book Now</span></span></a><!--[if mso]></center></v:textbox></v:roundrect><![endif]--></div> </td> </tr> </table> </div> </td> </tr> </tbody> </table> </td> </tr> </tbody> </table>''')

            ## random flights title
            email_file.write('''<table class="row row-5" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"> <tbody> <tr> <td> <table class="row-content" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-radius: 0; color: #000000; width: 640px; margin: 0 auto;" width="640"> <tbody> <tr> <td class="column column-1" width="25%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: middle; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"> <div class="spacer_block block-1" style="height:80px;line-height:80px;font-size:1px;">&#8202;</div> <table class="icons_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; text-align: center;"> <tr> <td class="pad" style="vertical-align: middle; color: #000000; font-family: inherit; font-size: 14px; font-weight: 400; text-align: center;"> <table class="icons-outer" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; display: inline-table;"> <tr> <td style="vertical-align: middle; text-align: center; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px;"><img class="icon" src="https://49733c35f1.imgdist.com/pub/bfra/sioce2wl/p16/33n/seu/dev-icon-218.svg" height="auto" width="32" align="center" style="display: block; height: auto; margin: 0 auto; border: 0;"></td> </tr> </table> </td> </tr> </table> </td> <td class="column column-2" width="75%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: middle; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"> <div class="spacer_block block-1" style="height:80px;line-height:80px;font-size:1px;">&#8202;</div> <table class="heading_block block-2" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"> <tr> <td class="pad"> <h3 style="margin: 0; color: #000000; direction: ltr; font-family: 'Bitter', Georgia, Times, 'Times New Roman', serif; font-size: 24px; font-weight: 700; letter-spacing: normal; line-height: 120%; text-align: left; margin-top: 0; margin-bottom: 0; mso-line-height-alt: 28.799999999999997px;"><span class="tinyMce-placeholder">...and find secret gems</span></h3> </td> </tr> </table> </td> </tr> </tbody> </table> </td> </tr> </tbody> </table>''')

            ## random flights
            if not random_flights:
                email_file.write(f'''<table class="row" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tbody><tr><td><table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 640px; margin: 0 auto;" width="640"><tbody><tr><td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"><table class="image_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tbody><tr><td class="pad" style="width:100%;padding-right:0px;padding-left:0px;"><div class="alignment" align="center" style="line-height:10px"><div style="max-width: 128px;"><img src="https://media0.giphy.com/media/qeEww6HA0rCPYzZ2PD/giphy.gif?cid=20eb4e9d4u0um05tuxu3jygzqxasv9s9yk9ftzyxj5bds6ff&amp;ep=v1_stickers_search&amp;rid=giphy.gif&amp;ct=s" style="display: block; height: auto; border: 0; width: 100%;" width="128" height="auto"></div></div></td></tr></tbody></table><table class="text_block block-2" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;"><tbody><tr><td class="pad"><div style="font-family: Georgia, 'Times New Roman', serif"><div class="" style="font-size: 12px; font-family: 'Bitter', Georgia, Times, 'Times New Roman', serif; mso-line-height-alt: 14.399999999999999px; color: #555555; line-height: 1.2;"><p style="margin: 0; font-size: 16px; text-align: center; mso-line-height-alt: 19.2px;"><strong>No Flights</strong><strong> Fou</strong><strong>nd</strong></p></div></div></td></tr></tbody></table><table class="text_block block-3" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;"><tbody><tr><td class="pad"><div style="font-family: Georgia, 'Times New Roman', serif"><div class="" style="font-size: 12px; font-family: 'Bitter', Georgia, Times, 'Times New Roman', serif; mso-line-height-alt: 18px; color: #555555; line-height: 1.5;"><p style="margin: 0; font-size: 15px; text-align: center; mso-line-height-alt: 21px; letter-spacing: normal;">Unfortunately, we couldn't find any flight deals for your secret gems. This may be due to limited flight availability to these countries or if you've favorited a large number of countries, leaving none remaining. You can update your profile using the button below.</p></div></div></td></tr></tbody></table><table class="button_block block-4" width="100%" border="0" cellpadding="5" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"><tbody><tr><td class="pad"><div class="alignment" align="center"><!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" 
                                href="https://www.timonrieger.com/projects/air-nomad-society/subscribe?token={user['token']}" style="height:34px;width:147px;v-text-anchor:middle;" arcsize="12%" stroke="false" fillcolor="#7747ff"><w:anchorlock/><v:textbox inset="0px,0px,0px,0px"><center style="color:#ffffff; font-family:Georgia, 'Times New Roman', serif; font-size:16px"><![endif]--><a href="https://www.timonrieger.com/projects/air-nomad-society/subscribe?token={user['token']}" style="text-decoration:none;display:inline-block;color:#ffffff;background-color:#7747ff;border-radius:4px;width:auto;border-top:0px solid transparent;font-weight:600;border-right:0px solid transparent;border-bottom:0px solid transparent;border-left:0px solid transparent;padding-top:5px;padding-bottom:5px;font-family:'Bitter', Georgia, Times, 'Times New Roman', serif;font-size:16px;text-align:center;mso-border-alt:none;word-break:keep-all;"><span style="padding-left:20px;padding-right:20px;font-size:16px;display:inline-block;letter-spacing:normal;"><span style="word-break: break-word; line-height: 24px;">Update Profile</span></span></a><!--[if mso]></center></v:textbox></v:roundrect><![endif]--></div></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table>''')
            else:
                for flight in random_flights:
                    try:
                        images = image_data[flight['arr_country']]
                    except KeyError:
                        url = "https://images.unsplash.com/photo-1500835556837-99ac94a94552?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8VFJBVkVMfGVufDB8fDB8fHww"
                    else:
                        url = random.choice(images)
                    if random_flights.index(flight) % 2 == 0:
                        email_file.write(f'''<table class="row row-6" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"> <tbody> <tr> <td> <table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-radius: 0; color: #000000; width: 640px; margin: 0 auto;" width="640"> <tbody> <tr> <td class="column column-1" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: bottom; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"> <div class="spacer_block block-1" style="height:60px;line-height:60px;font-size:1px;">&#8202;</div> <table class="paragraph_block block-2" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;"> <tr> <td class="pad"> <div style="color:#444a5b;direction:ltr;font-family:'Bitter', Georgia, Times, 'Times New Roman', serif;font-size:18px;font-weight:300;letter-spacing:0px;line-height:120%;text-align:center;mso-line-height-alt:21.599999999999998px;"> <p style="margin: 0; margin-bottom: 16px;">
                                          <strong>{flight['price']} {flight['currency']}</strong><br><br><strong>{flight['dep_city']}</strong> - <strong>{flight['arr_city']}</strong></p> <p style="margin: 0;">in {flight['arr_country']}</strong><br><br><strong>{flight['from_dt']} - {flight['to_dt']}</strong></p> </div> </td> </tr> </table> <table class="button_block block-3" width="100%" border="0" cellpadding="5" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"> <tr> <td class="pad"> <div class="alignment" align="center"><!--[if mso]> <v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href={flight['link']} style="height:34px;width:115px;v-text-anchor:middle;" arcsize="12%" stroke="false" fillcolor="#7747ff"> <w:anchorlock/> <v:textbox inset="0px,0px,0px,0px"> <center style="color:#ffffff; font-family:Georgia, 'Times New Roman', serif; font-size:16px"> <![endif]--><a 
                                          href={flight['link']} style="text-decoration:none;display:inline-block;color:#ffffff;background-color:#7747ff;border-radius:4px;width:auto;border-top:0px solid transparent;font-weight:600;border-right:0px solid transparent;border-bottom:0px solid transparent;border-left:0px solid transparent;padding-top:5px;padding-bottom:5px;font-family:'Bitter', Georgia, Times, 'Times New Roman', serif;font-size:16px;text-align:center;mso-border-alt:none;word-break:keep-all;"><span style="padding-left:20px;padding-right:20px;font-size:16px;display:inline-block;letter-spacing:normal;"><span style="word-break: break-word; line-height: 24px;">Book Now</span></span></a><!--[if mso]></center></v:textbox></v:roundrect><![endif]--></div> </td> </tr> </table> </td> <td class="column column-2" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: bottom; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"> <table class="image_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"> <tr> <td class="pad" style="width:100%;"> <div class="alignment" align="center" style="line-height:10px"> <div style="max-width: 320px; max-height: 200px;"><img src={url} style="display: block; height: 200px; width:100%; border: 0; border-radius: 10px;"
    ></div> </div> </td> </tr> </table> </td> </tr> </tbody> </table> </td> </tr> </tbody> </table>''')
                    else:
                        email_file.write(f'''<table class="row row-7" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"> <tbody> <tr> <td> <table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-radius: 0; color: #000000; width: 640px; margin: 0 auto;" width="640"> <tbody> <tr class="reverse"> <td class="column column-1 first" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: bottom; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"> <div class="border"> <table class="image_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"> <tr> <td class="pad" style="width:100%;"> <div class="alignment" align="center" style="line-height:10px"> <div style="max-width: 320px; max-height: 200px;"><img src={url} style="display: block; height: 200px; width:100%; border: 0; border-radius: 10px;"
    ></div> </div> </td> </tr> </table> </div> </td> <td class="column column-2 last" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: bottom; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"> <div class="border"> <div class="spacer_block block-1" style="height:60px;line-height:60px;font-size:1px;">&#8202;</div> <table class="paragraph_block block-2" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;"> <tr> <td class="pad"> <div style="color:#444a5b;direction:ltr;font-family:'Bitter', Georgia, Times, 'Times New Roman', serif;font-size:18px;font-weight:300;letter-spacing:0px;line-height:120%;text-align:center;mso-line-height-alt:21.599999999999998px;"> <p style="margin: 0; margin-bottom: 16px;">
                                          <strong>{flight['price']} {flight['currency']}</strong><br><br><strong>{flight['dep_city']}</strong> - <strong>{flight['arr_city']}</strong></p> <p style="margin: 0;">in {flight['arr_country']}</strong><br><br><strong>{flight['from_dt']} - {flight['to_dt']}</strong></p> </div> </td> </tr> </table> <table class="button_block block-3" width="100%" border="0" cellpadding="5" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"> <tr> <td class="pad"> <div class="alignment" align="center"><!--[if mso]> <v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href={flight['link']} style="height:34px;width:115px;v-text-anchor:middle;" arcsize="12%" stroke="false" fillcolor="#7747ff"> <w:anchorlock/> <v:textbox inset="0px,0px,0px,0px"> <center style="color:#ffffff; font-family:Georgia, 'Times New Roman', serif; font-size:16px"> <![endif]--><a 
                                          href={flight['link']} style="text-decoration:none;display:inline-block;color:#ffffff;background-color:#7747ff;border-radius:4px;width:auto;border-top:0px solid transparent;font-weight:600;border-right:0px solid transparent;border-bottom:0px solid transparent;border-left:0px solid transparent;padding-top:5px;padding-bottom:5px;font-family:'Bitter', Georgia, Times, 'Times New Roman', serif;font-size:16px;text-align:center;mso-border-alt:none;word-break:keep-all;"><span style="padding-left:20px;padding-right:20px;font-size:16px;display:inline-block;letter-spacing:normal;"><span style="word-break: break-word; line-height: 24px;">Book Now</span></span></a><!--[if mso]></center></v:textbox></v:roundrect><![endif]--></div> </td> </tr> </table> </div> </td> </tr> </tbody> </table> </td> </tr> </tbody> </table>''')

            ## end
            email_file.write('''<table class="row row-8" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"> <tbody> <tr> <td> <table class="row-content" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-radius: 0; color: #000000; width: 640px; margin: 0 auto;" width="640"> <tbody> <tr> <td class="column column-1" width="58.333333333333336%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: middle; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"> <table class="heading_block block-1" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"> <tr> <td class="pad"> <h1 style="margin: 0; color: #000000; direction: ltr; font-family: 'Bitter', Georgia, Times, 'Times New Roman', serif; font-size: 38px; font-weight: 700; letter-spacing: normal; line-height: 120%; text-align: center; margin-top: 0; margin-bottom: 0; mso-line-height-alt: 45.6px;">Happy Travels!</h1> </td> </tr> </table> </td> <td class="column column-2" width="41.666666666666664%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: middle; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"> <div class="spacer_block block-1" style="height:20px;line-height:20px;font-size:1px;">&#8202;</div> <table class="image_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"> <tr> <td class="pad" style="width:100%;"> <div class="alignment" align="center" style="line-height:10px"> <div style="max-width: 266.667px;"><img src="https://media0.giphy.com/media/jDPJmNhDsTV9OviMkv/giphy.gif?cid=20eb4e9dr0de8whfboq1as0nrvucnf7zkeuzqu9zmu5vfg5l&ep=v1_stickers_search&rid=giphy.gif&ct=s" style="display: block; height: auto; border: 0; width: 100%;" width="266.667" height="auto"></div> </div> </td> </tr> </table> <div class="spacer_block block-3" style="height:20px;line-height:20px;font-size:1px;">&#8202;</div> </td> </tr> </tbody> </table> </td> </tr> </tbody> </table>'''
                             f'''<table class="row row-9" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"> <tbody> <tr> <td> <table class="row-content" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-radius: 0px; color: rgb(0, 0, 0); width: 640px; margin: 0px auto; --darkreader-inline-color: #e8e6e3;" width="640" data-darkreader-inline-color=""> <tbody> <tr> <td class="column column-1" width="50%" style="font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: middle; border-width: 0px; border-style: initial; border-color: initial; --darkreader-inline-border-top: 0px; --darkreader-inline-border-right: 0px; --darkreader-inline-border-bottom: 0px; --darkreader-inline-border-left: 0px;" data-darkreader-inline-border-top="" data-darkreader-inline-border-right="" data-darkreader-inline-border-bottom="" data-darkreader-inline-border-left=""> <table class="menu_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"> <tbody><tr> <td class="pad" style="color: rgb(0, 0, 0); font-family: Bitter, Georgia, Times, &quot;Times New Roman&quot;, serif; font-size: 12px; font-weight: 300; letter-spacing: 0px; text-align: center; --darkreader-inline-color: #e8e6e3;" data-darkreader-inline-color=""> <table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
																			<tbody><tr> <td class="alignment" style="text-align:center;font-size:0px;"> <div class="menu-links"><!--[if mso]><table role="presentation" border="0" cellpadding="0" cellspacing="0" align="center" style=""><tr style="text-align:center;"><![endif]--><!--[if mso]><td style="padding-top:5px;padding-right:10px;padding-bottom:5px;padding-left:10px"><![endif]--><a href="https://www.timonrieger.com" target="_self" style="padding: 5px 10px; display: inline-block; color: rgb(0, 0, 0); font-family: Bitter, Georgia, Times, &quot;Times New Roman&quot;, serif; font-size: 12px; text-decoration: none; letter-spacing: normal; --darkreader-inline-color: #e8e6e3;" data-darkreader-inline-color="">timonrieger.com</a><!--[if mso]></td><![endif]--><!--[if mso]><td style="padding-top:5px;padding-right:10px;padding-bottom:5px;padding-left:10px"><![endif]--><a href="https://www.timonrieger.com/unsubscribe?token={user['token']}&amp;form=ans" target="_self" style="padding: 5px 10px; display: inline-block; color: rgb(0, 0, 0); font-family: Bitter, Georgia, Times, &quot;Times New Roman&quot;, serif; font-size: 12px; text-decoration: none; letter-spacing: normal; --darkreader-inline-color: #e8e6e3;" data-darkreader-inline-color="">Unsubscribe</a><!--[if mso]></td><![endif]--><!--[if mso]><td style="padding-top:5px;padding-right:10px;padding-bottom:5px;padding-left:10px"><![endif]--><a href="https://www.timonrieger.com/projects/air-nomad-society/subscribe?token={user['token']}" target="_self" style="padding: 5px 10px; display: inline-block; color: rgb(0, 0, 0); font-family: Bitter, Georgia, Times, &quot;Times New Roman&quot;, serif; font-size: 12px; text-decoration: none; letter-spacing: normal; --darkreader-inline-color: #e8e6e3;" data-darkreader-inline-color="">Update Profile</a><!--[if mso]></td><![endif]--><!--[if mso]></tr></table><![endif]--></div> </td> </tr> </tbody></table> </td> </tr> </tbody></table> <div class="spacer_block block-2" style="height:40px;line-height:40px;font-size:1px;"> </div> </td> </tr> </tbody> </table> </td> </tr> </tbody> </table><!-- End --> </body> </html>''')

            email_file.close()

        # Create a multipart message
        msg = MIMEMultipart()
        msg['From'] = f"Air Nomad Society <{ANS_EMAIL}>"
        msg['To'] = user["email"]
        msg['Subject'] = "Weekly Flight Deals!"
        # Read HTML file
        with open('templates/weekly_ans_email/user_mail.html', 'r', encoding="utf-8") as email_file:
            html_string = email_file.read()

        # Attach HTML content to the email
        html_part = MIMEText(html_string, 'html', 'utf-8')  # Specify charset

        # Set content-transfer-encoding explicitly to base64
        html_part.set_param('charset', 'utf-8')
        html_part.set_param('Content-Transfer-Encoding', 'base64')

        msg.attach(html_part)

        with smtplib.SMTP_SSL(host="smtp.gmail.com") as connection:
            connection.login(user=ANS_EMAIL, password=ANS_MAIL_PASSWORD)
            connection.send_message(msg)
            connection.close()

        # clear unique html file
        with open('templates/weekly_ans_email/user_mail.html', "w") as email_file:
            email_file.write("")

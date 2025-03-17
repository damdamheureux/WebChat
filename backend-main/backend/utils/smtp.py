import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
try:
    from ..config import base_url
except:
    base_url = "http://localhost:8000"
sender_email = "admin@vonelstudio.online"
receiver_email = "me@saturna19.fr"
password = "SaturnaDev"

message = MIMEMultipart("alternative")
message["Subject"] = "Verify your account"
message["From"] = sender_email
message["To"] = receiver_email
#Placeholders: 
# {USER_FIRNAME_PH} {USER_LASNAME_PH}

def generate_template(templateName: str ):
    return {}

def generate_email_string(firstname, lastname, token):
    return """\
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en"><head><meta charset="UTF-8"><meta content="width=device-width, initial-scale=1" name="viewport"><meta name="x-apple-disable-message-reformatting"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta content="telephone=no" name="format-detection"><title>New email template 2025-02-05</title> <!--[if (mso 16)]><style type="text/css"> a {text-decoration: none;}  </style><![endif]--><!--[if gte mso 9]><style>sup { font-size: 100% !important; }</style><![endif]--><!--[if gte mso 9]><noscript> <xml> <o:OfficeDocumentSettings> <o:AllowPNG></o:AllowPNG> <o:PixelsPerInch>96</o:PixelsPerInch> </o:OfficeDocumentSettings> </xml> </noscript>
<![endif]--><!--[if mso]><xml> <w:WordDocument xmlns:w="urn:schemas-microsoft-com:office:word"> <w:DontUseAdvancedTypographyReadingMail/> </w:WordDocument> </xml>
<![endif]--><style type="text/css">.rollover:hover .rollover-first { max-height:0px!important; display:none!important;}.rollover:hover .rollover-second { max-height:none!important; display:block!important;}.rollover span { font-size:0px;}u + .body img ~ div div { display:none;}#outlook a { padding:0;}span.MsoHyperlink,span.MsoHyperlinkFollowed { color:inherit; mso-style-priority:99;}a.a { mso-style-priority:100!important; text-decoration:none!important;}a[x-apple-data-detectors],#MessageViewBody a { color:inherit!important; text-decoration:none!important; font-size:inherit!important; font-family:inherit!important; font-weight:inherit!important; line-height:inherit!important;}.e { display:none; float:left; overflow:hidden; width:0; max-height:0; line-height:0; mso-hide:all;}.r:hover { border-color:#3d5ca3 #3d5ca3 #3d5ca3 #3d5ca3!important; background:#ffffff!important;}.r:hover a.a,.r:hover button.a { background:#ffffff!important;}
.r:hover a.a { background:#ffffff!important; border-color:#ffffff!important;}@media only screen and (max-width:600px) { *[class="gmail-fix"] { display:none!important } p, a { line-height:150%!important } h1, h1 a { line-height:120%!important } h2, h2 a { line-height:120%!important } h3, h3 a { line-height:120%!important } h4, h4 a { line-height:120%!important } h5, h5 a { line-height:120%!important } h6, h6 a { line-height:120%!important } .z p { } .y p { } .x p { } h1 { font-size:20px!important; text-align:center; line-height:120%!important } h2 { font-size:16px!important; text-align:left; line-height:120%!important } h3 { font-size:20px!important; text-align:center; line-height:120%!important } h4 { font-size:24px!important; text-align:left } h5 { font-size:20px!important; text-align:left } h6 { font-size:16px!important; text-align:left } .z p, .z a { font-size:16px!important } .y p, .y a { font-size:12px!important }
 .x p, .x a { font-size:12px!important } .t .rollover:hover .rollover-second, .u .rollover:hover .rollover-second, .v .rollover:hover .rollover-second { display:inline!important } a.a, button.a { font-size:14px!important; padding:10px 20px 10px 20px!important; line-height:120%!important } a.a, button.a, .r { display:inline-block!important } .k table, .l, .m { width:100%!important } .h table, .i table, .j table, .h, .j, .i { width:100%!important; max-width:600px!important } .adapt-img { width:100%!important; height:auto!important } .h-auto { height:auto!important } h2 a { text-align:left } a.a { border-left-width:0px!important; border-right-width:0px!important } }@media screen and (max-width:384px) {.mail-message-content { width:414px!important } }</style>
 </head> <body class="body" style="width:100%;height:100%;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;padding:0;Margin:0"><div dir="ltr" class="es-wrapper-color" lang="en" style="background-color:#FAFAFA"><!--[if gte mso 9]><v:background xmlns:v="urn:schemas-microsoft-com:vml" fill="t"> <v:fill type="tile" color="#fafafa"></v:fill> </v:background><![endif]--><table width="100%" cellspacing="0" cellpadding="0" class="es-wrapper" role="none" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;padding:0;Margin:0;width:100%;height:100%;background-repeat:repeat;background-position:center top;background-color:#FAFAFA"><tr style="border-collapse:collapse">
<td valign="top" style="padding:0;Margin:0"><table cellpadding="0" cellspacing="0" align="center" class="h" role="none" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;width:100%;table-layout:fixed !important"><tr style="border-collapse:collapse"><td align="center" class="k" style="padding:0;Margin:0"><table cellspacing="0" cellpadding="0" bgcolor="#ffffff" align="center" class="z" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:transparent;width:600px" role="none"><tr style="border-collapse:collapse"><td align="left" style="padding:10px;Margin:0"><table width="100%" cellspacing="0" cellpadding="0" role="none" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"><tr style="border-collapse:collapse">
<td valign="top" align="center" style="padding:0;Margin:0;width:580px"><table width="100%" cellspacing="0" cellpadding="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"><tr style="border-collapse:collapse"><td align="center" class="x" style="padding:0;Margin:0"><p style="Margin:0;mso-line-height-rule:exactly;font-family:helvetica, 'helvetica neue', arial, verdana, sans-serif;line-height:24px;letter-spacing:0;color:#CCCCCC;font-size:16px">If you're not able to see this mail, please contact admin@vonelstudio.online</p> </td></tr></table></td></tr></table></td></tr></table></td></tr></table> <table cellspacing="0" cellpadding="0" align="center" class="h" role="none" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;width:100%;table-layout:fixed !important"><tr style="border-collapse:collapse">
<td bgcolor="#fafafa" align="center" style="padding:0;Margin:0;background-color:#FAFAFA"><table cellspacing="0" cellpadding="0" bgcolor="#ffffff" align="center" class="z" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#FFFFFF;width:600px" role="none"><tr style="border-collapse:collapse"><td bgcolor="transparent" align="left" style="padding:0;Margin:0;padding-top:40px;padding-right:20px;padding-left:20px;background-color:transparent;background-position:left top"><table width="100%" cellspacing="0" cellpadding="0" role="none" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"><tr style="border-collapse:collapse">
<td valign="top" align="center" style="padding:0;Margin:0;width:560px"><table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-position:left top" role="presentation"><tr style="border-collapse:collapse"><td align="center" style="padding:0;Margin:0;padding-top:5px;padding-bottom:5px;font-size:0"><img src="https://fkfgntn.stripocdn.email/content/guids/CABINET_dd354a98a803b60e2f0411e893c82f56/images/23891556799905703.png" alt="" width="175" style="display:block;font-size:14px;border:0;outline:none;text-decoration:none"></td> </tr><tr style="border-collapse:collapse">
<td align="center" style="padding:0;Margin:0;padding-top:15px;padding-bottom:15px"><h1 style="Margin:0;font-family:arial, 'helvetica neue', helvetica, sans-serif;mso-line-height-rule:exactly;letter-spacing:0;font-size:20px;font-style:normal;font-weight:normal;line-height:24px;color:#333333"><strong>FORGOT YOUR </strong></h1><h1 style="Margin:0;font-family:arial, 'helvetica neue', helvetica, sans-serif;mso-line-height-rule:exactly;letter-spacing:0;font-size:20px;font-style:normal;font-weight:normal;line-height:24px;color:#333333"><strong>&nbsp;PASSWORD?</strong></h1></td></tr> <tr style="border-collapse:collapse"><td align="left" style="padding:0;Margin:0;padding-right:40px;padding-left:40px"><p style="Margin:0;mso-line-height-rule:exactly;font-family:helvetica, 'helvetica neue', arial, verdana, sans-serif;line-height:24px;letter-spacing:0;color:#666666;font-size:16px;text-align:center">HI,&nbsp;%FIRSTNAME|% %LASTNAME|%</p></td></tr>
<tr style="border-collapse:collapse"><td align="left" style="padding:0;Margin:0;padding-left:40px;padding-right:35px"><p style="Margin:0;mso-line-height-rule:exactly;font-family:helvetica, 'helvetica neue', arial, verdana, sans-serif;line-height:24px;letter-spacing:0;color:#666666;font-size:16px;text-align:center">There was a request to change your password!</p></td></tr> <tr style="border-collapse:collapse"><td align="center" style="padding:0;Margin:0;padding-right:40px;padding-left:40px;padding-top:25px"><p style="Margin:0;mso-line-height-rule:exactly;font-family:helvetica, 'helvetica neue', arial, verdana, sans-serif;line-height:24px;letter-spacing:0;color:#666666;font-size:16px">If did not make this request, just ignore this email. Otherwise, please click the button below to change your password:</p></td></tr> <tr style="border-collapse:collapse">
<td align="center" style="Margin:0;padding-top:40px;padding-right:10px;padding-bottom:40px;padding-left:10px"><span class="r" style="border-style:solid;border-color:#3D5CA3;background:#FFFFFF;border-width:2px;display:inline-block;border-radius:10px;width:auto"><a href="%TOKENVERIFICATIONLINK%" target="_blank" class="a" style="mso-style-priority:100 !important;text-decoration:none !important;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;font-size:14px;color:#3D5CA3;padding:10px 20px 10px 20px;display:inline-block;background:#FFFFFF;border-radius:10px;font-weight:bold;font-style:normal;line-height:16.8px;width:auto;text-align:center;letter-spacing:0;mso-padding-alt:0;mso-border-alt:10px solid #FFFFFF">Verify my account</a></span></td></tr></table></td></tr></table></td></tr></table></td></tr></table>
 <table cellspacing="0" cellpadding="0" align="center" class="j" role="none" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;width:100%;table-layout:fixed !important;background-color:transparent;background-repeat:repeat;background-position:center top"><tr style="border-collapse:collapse"><td bgcolor="#fafafa" align="center" style="padding:0;Margin:0;background-color:#FAFAFA"><table cellspacing="0" cellpadding="0" bgcolor="#ffffff" align="center" class="y" role="none" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:transparent;width:600px"><tr style="border-collapse:collapse">
<td bgcolor="#0b5394" align="left" style="Margin:0;padding-right:20px;padding-left:20px;padding-top:10px;padding-bottom:30px;background-color:#0B5394;background-position:left top"><table width="100%" cellspacing="0" cellpadding="0" role="none" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"><tr style="border-collapse:collapse"><td valign="top" align="center" style="padding:0;Margin:0;width:560px"><table width="100%" cellspacing="0" cellpadding="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"><tr style="border-collapse:collapse">
<td align="left" style="padding:0;Margin:0;padding-top:5px;padding-bottom:5px"><h2 style="Margin:0;font-family:arial, 'helvetica neue', helvetica, sans-serif;mso-line-height-rule:exactly;letter-spacing:0;font-size:16px;font-style:normal;font-weight:normal;line-height:19.2px;color:#ffffff"><strong>Have quastions?</strong></h2> </td></tr><tr style="border-collapse:collapse"><td align="left" style="padding:0;Margin:0;padding-bottom:5px"><p style="Margin:0;mso-line-height-rule:exactly;font-family:helvetica, 'helvetica neue', arial, verdana, sans-serif;line-height:21px;letter-spacing:0;color:#ffffff;font-size:14px">We are here to help, learn more about us <a target="_blank" style="mso-line-height-rule:exactly;text-decoration:none;font-family:helvetica, 'helvetica neue', arial, verdana, sans-serif;font-size:14px;color:#ffffff" href="">here</a></p>
<p style="Margin:0;mso-line-height-rule:exactly;font-family:helvetica, 'helvetica neue', arial, verdana, sans-serif;line-height:21px;letter-spacing:0;color:#ffffff;font-size:14px">or <a target="_blank" style="mso-line-height-rule:exactly;text-decoration:none;font-family:helvetica, 'helvetica neue', arial, verdana, sans-serif;font-size:14px;color:#ffffff" href="">contact us</a><br></p></td></tr></table></td> </tr></table></td></tr></table></td></tr></table><table cellspacing="0" cellpadding="0" align="center" class="h" role="none" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;width:100%;table-layout:fixed !important"></table>
<table cellspacing="0" cellpadding="0" align="center" class="j" role="none" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;width:100%;table-layout:fixed !important;background-color:transparent;background-repeat:repeat;background-position:center top"></table><table cellspacing="0" cellpadding="0" align="center" class="h" role="none" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;width:100%;table-layout:fixed !important"></table></td></tr></table></div></body></html>
""".replace("%FIRSTNAME|%", firstname).replace("%LASTNAME|%", lastname).replace("%TOKENVERIFICATIONLINK%", f"{base_url}/auth/account/verify?token={token}")


# Turn these into plain/html MIMEText objects
part2 = MIMEText(generate_email_string("Thibault", "MOREZ", "alpha"), "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("mail.vonelstudio.online", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
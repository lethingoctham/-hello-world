# -*- coding: utf-8 -*-
"""

@author: acer
"""

import smtplib
server = smtplib.SMTP('smtp.gmail.com', 578 )
server.starttls()
server.login("gaupooh456@gail.com", "gaupooh1234")
msg = "hi tbrbt"
server.sendmail("gaupooh456@gmail.com", "ndhcuong@hueuni.edu.vn", msg)
server.quit()

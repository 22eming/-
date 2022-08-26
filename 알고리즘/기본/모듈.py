import theater_module
theater_module.price(3)
theater_module.price_moring(4)
theater_module.price_soldier(5)

import theater_module as mv #theater_module 을 mv로 변경
mv.price(3)

from theater_module import*
price(3)

from theater_module import price, price_moring
price(5)
price_moring(6)

from theater_module import price_soldier as ps
ps(5)
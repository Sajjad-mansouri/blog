
import jdatetime

def persian_number_converter(number):
    numbers = {
		"0": "۰",
		"1": "۱",
		"2": "۲",
		"3": "۳",
		"4": "۴",
		"5": "۵",
		"6": "۶",
		"7": "۷",
		"8": "۸",
		"9": "۹",
	}

    for e,p in numbers.items():
        number= number.replace(e,p)
    return number

def shamsi_converter(time):
    jmonths = ['فروردین','اردیبهشت','خرداد','تیر','مرداد','شهریور','مهر','آبان','آذر','دی','بهمن','اسفند']

    date=jdatetime.date.fromgregorian(day=time.day,month=time.month,year=time.year)
    date_list={date}
    for index , pmonth in  enumerate(jmonths):
        if date.month== index+1:
            converted_month= pmonth
            break
    
    output=f'{date.day} {converted_month} {date.year} , ساعت {time.minute}:{time.hour}'
    
    return persian_number_converter(output)
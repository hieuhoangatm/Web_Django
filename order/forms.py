from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
	DIVISION_CHOICES = (		
		('Hà Nội', 'Hà Nội'),
		('Hà Nam', 'Hà Nam'),
	)

	DISCRICT_CHOICES = (
		
		('Hà Đông', 'Ha Đông'),
		('Thanh Xuân', 'Thanh Xuân'),
		('Nam Từ Liêm', 'Nam Từ Liêm'),
		('Hai Bà Trưng', 'Hai Bà Trưng'),
		('Long Biên', 'Long Biên'),
		('Ba Đình', 'Ba Đình'),
		('Cầu Giấy', 'Cầu Giấy'),
		('Bắc Từ Liêm', 'Bắc Từ Liêm'),
		('Hoàng Mai', 'Hoàng Mai'),
		('Đống Đa', 'Đống Đa'),
		('Hoàn Kiếm', 'Hoàn Kiếm'),
		('Tây Hồ', 'Tây Hồ'),
	)

	PAYMENT_METHOD_CHOICES = (
		('Chuyển phát nhanh', 'Chuyển phát nhanh'),
		('Thông thường','Thông thường')
	)

	division = forms.ChoiceField(choices=DIVISION_CHOICES)
	district =  forms.ChoiceField(choices=DISCRICT_CHOICES)
	payment_method = forms.ChoiceField(choices=PAYMENT_METHOD_CHOICES, widget=forms.RadioSelect())

	class Meta:
		model = Order
		fields = ['name', 'email', 'phone', 'address', 'division', 'district', 'zip_code', 'payment_method', 'account_no', 'transaction_id']

from django.contrib import admin, messages
from django.urls import path, reverse
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.html import format_html

from django.core.exceptions import FieldDoesNotExist
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render

from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render


class OptionsShow:
    """
    一个用于标记字段需要特殊显示逻辑的标志类。
    """
    pass


class PdfAdmin(admin.ModelAdmin):
    pdf_fields = []
    option_fields = []
    pdf_title = ''
    right_tip = ''
    left_tip = ''
    pdf_template = 'pdfExport/base_pdf_template.html'
    change_form_template = 'pdfExport/pdf_export_change_form.html'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('pdf_export/<int:pk>/', self.admin_site.admin_view(self.pdf_export), name='pdf_export'),
        ]
        return custom_urls + urls

    def pdf_show(self, obj):
        return format_html('<a class="button" href="{}">PDF导出</a>',
                           reverse('admin:pdf_export', args=[obj.pk]))

    pdf_show.short_description = 'PDF导出'
    pdf_show.allow_tags = True

    def pdf_export(self, request, pk):
        context = self.get_pdf_context(pk)
        context['title'] = self.pdf_title
        context['right_tip'] = self.right_tip
        context['left_tip'] = self.left_tip
        return render(request, self.pdf_template, context)

    class PdfAdmin(admin.ModelAdmin):
        pdf_fields = []
        pdf_title = ''

    def get_pdf_context(self, pk):
        obj = self.model.objects.get(pk=pk)
        grouped_fields = []
        option_fields = self.option_fields if hasattr(self, 'option_fields') else []

        for item in self.pdf_fields:
            if isinstance(item, tuple):
                # 检查元组的第二个元素类型，判断是带标题的组合还是仅字段组合
                if isinstance(item[1], set):
                    # 处理带有组标题和字段组的项
                    group_title, fields_set = item
                    field_group = {"group_title": group_title, "fields": []}
                    for sub_field_tuple in fields_set:
                        for sub_field in sub_field_tuple:
                            field_obj = self.model._meta.get_field(sub_field)
                            field_data = self.process_field(field_obj, obj, sub_field, option_fields)
                            field_group["fields"].append(field_data)
                    grouped_fields.append(field_group)
                else:
                    # 处理仅为字段名称组合的元组
                    field_group = {"group_title": None, "fields": []}
                    for sub_field in item:
                        field_obj = self.model._meta.get_field(sub_field)
                        field_data = self.process_field(field_obj, obj, sub_field, option_fields)
                        field_group["fields"].append(field_data)
                    grouped_fields.append(field_group)
            else:
                # 处理单独的字段名称
                field_obj = self.model._meta.get_field(item)
                field_data = self.process_field(field_obj, obj, item, option_fields)
                grouped_fields.append({"group_title": None, "fields": [field_data]})

        return {"grouped_fields": grouped_fields}

    def process_field(self, field_obj, obj, field_name, option_fields):
        """处理单个字段，获取其详细信息"""
        if field_name in option_fields:
            # 选项字段处理逻辑
            all_options = field_obj.related_model.objects.all()
            current_option = getattr(obj, field_name, None)
            options_list = [{'name': str(option), 'selected': (option == current_option)} for option in all_options]
            return {
                "verbose_name": field_obj.verbose_name,
                "value": options_list,
                "is_option_field": True
            }
        else:
            # 非选项字段处理逻辑
            return {
                "verbose_name": field_obj.verbose_name,
                "value": getattr(obj, field_name, ''),
                "is_option_field": False
            }

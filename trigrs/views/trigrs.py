from trigrs.models import DataTrigrs, DataTrigrsDetail
from django.conf import settings
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import io
from django.core.files.storage import FileSystemStorage
from datetime import datetime
import os

msg = ''


@login_required(login_url="/login/")
def data_trigrs(request):
    dataAll = []
    mess = ''
    data = DataTrigrs.objects.all()
    for i in data:

        dataDetail = DataTrigrsDetail.objects.filter(trigrs_id=i.id)
        dataD = []
        count = 0
        for a in dataDetail:

            context_data_detail = {
                "id": a.id,
                "data_added": a.data_added,
                "data_updated": a.data_updated,
                "ch": a.ch,
                "filename": a.filename,
                "file_upload_status": a.file_upload_status
            }

            count = count + 1
            dataD.append(context_data_detail)

        context_data = {
            "id": i.id,
            "key_id": i.key_id,
            "data_name": i.data_name,
            "detail_count": count,
            "detail": dataD,

        }
        dataAll.append(context_data)

    # if request.method == 'POST':

        if 'edit' in request.POST:
            data_edit = DataTrigrsDetail.objects.get(
                id=request.POST.get('edit'))
            return render(request, 'main/edit-data-trigrs.html', {'data_edit': data_edit})
    #     if 'save' in request.POST:
    #         client = ClientAdmin.objects.get(user=request.user)

    #         try:
    #             contact_save = Contact.objects.get(
    #                 id=request.POST.get('id'), company=client.company)
    #         except Contact.DoesNotExist:
    #             contact_save = None

    #         if contact_save:
    #             contact_save.contact_name = request.POST.get('name')
    #             contact_save.contact_address = request.POST.get('address')
    #             contact_save.contact_email = request.POST.get('email')
    #             contact_save.contact_phone = request.POST.get('phone')
    #             contact_save.contact_division = request.POST.get('division')
    #             contact_save.contact_branch = request.POST.get('branch')
    #             contact_save.contact_type = request.POST.get('type')

    #             if request.POST.get('active') == 'on':
    #                 contact_save.is_active = True
    #             else:
    #                 contact_save.is_active = False

    #             contact_save.save()
    #             mess = messages.success(request, 'Data berhasil diubah')

    #     data = []
    #     cons = Contact.objects.filter(company=client.company)

    #     for i in cons:
    #         try:
    #             case = Case.objects.filter(
    #                 contact=i, test_result=None)[0]
    #         except IndexError:
    #             case = None

    #         context = {
    #             "id": i.id,
    #             "name": i.contact_name,
    #             "company": i.company,
    #             "address": i.contact_address,
    #             "email": i.contact_email,
    #             "phone": i.contact_phone,
    #             "uid": i.contact_uid,
    #             "division": i.contact_division,
    #             "branch": i.contact_branch,
    #             "type": i.contact_type,
    #             "is_active": i.is_active,
    #             "case": case
    #         }
    #         data.append(context)

    #     return render(request, 'client/contact.html', {'org': client.company.organization_type, "company_name": client.company.company_name, 'contact': data, 'message': mess})

    return render(request, 'main/data-trigrs.html', {'data_trigrs': dataAll, 'message': mess})


@login_required(login_url="/login/")
def add_data_trigrs(request):
    if request.method == 'POST':
        if 'addData' in request.POST:
            trigrs = DataTrigrs()
            trigrs_detail = DataTrigrsDetail()

            trigrs.key_id = request.POST.get('id')
            trigrs.data_name = request.POST.get('name')
            trigrs.save()

            for x in range(int(request.POST.get('counter'))):

                dirname = datetime.now().strftime('%d%m%Y_%H%M%S')  # 09082010_120845
                os.mkdir(os.path.join('media/',
                                      request.POST.get(+dirname+'curah_hujan'+str(x+1))))
                filepath = request.FILES.get('file_input'+str(x+1), False)

                trigrs_detail.id = None
                trigrs_detail.data_added = timezone.now()
                trigrs_detail.ch = request.POST.get('curah_hujan'+str(x+1))
                trigrs_detail.filename = filepath.name
                trigrs_detail.file_upload_status = "Uploading"
                trigrs_detail.trigrs = trigrs
                trigrs_detail.save()

                myfile = request.FILES['file_input'+str(x+1)]
                fs = FileSystemStorage(location=os.path.join('media/',
                                                             request.POST.get('curah_hujan'+str(x+1))+'_'+dirname))
                fs.save(myfile.name, filepath)

                trigrs_detail.file_upload_status = "Uploaded"
                trigrs_detail.save()

            msg = messages.success(request, 'Data berhasil ditambahkan!')
            return redirect('/data-trigrs/')
    return render(request, 'main/add-data-trigrs.html', {})

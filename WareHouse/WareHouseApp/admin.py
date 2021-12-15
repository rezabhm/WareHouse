from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ["name", "company_id", ]

    fieldsets = (

        ("total information", {"fields": ("name", "company_id")}),

    )

    list_filter = ["name", ]


@admin.register(models.CEO)
class CEOAdmin(admin.ModelAdmin):
    list_display = ["name", "username", "lastname", "phone_number", "ceo_id", ]

    fieldsets = (

        ("personal information", {"fields": ("name", "username", "lastname", "phone_number", "ceo_id")}),
        ("relation information", {"fields": ("company", "user",)}),

    )

    list_filter = ["user name", ]


@admin.register(models.SalesManager)
class SalesManagerAdmin(admin.ModelAdmin):
    list_display = ["name", "username", "lastname", "phone_number", "sales_manager_id", ]

    fieldsets = (

        ("personal information", {"fields": ("name", "username", "lastname", "phone_number", "sales_manager_id")}),
        ("relation information", {"fields": ("company", "user",)}),

    )

    list_filter = ["user name", ]


@admin.register(models.WeightLiftingManager)
class WeightLiftingManagerAdmin(admin.ModelAdmin):
    list_display = ["name", "username", "lastname", "phone_number", "Weight_Lifting_Manager_id", ]

    fieldsets = (

        ("personal information", {"fields": ("name", "username", "lastname", "phone_number", "Weight_Lifting_Manager_id")}),
        ("relation information", {"fields": ("company", "user",)}),

    )

    list_filter = ["user name", ]


@admin.register(models.FreezingTunnelManager)
class FreezingTunnelManagerAdmin(admin.ModelAdmin):
    list_display = ["name", "username", "lastname", "phone_number", "Freezing_tunnel_Manager_id", ]

    fieldsets = (

        ("personal information", {"fields": ("name", "username",
        "lastname", "phone_number", "Freezing_tunnel_Manager_id", )}),
        ("relation information", {"fields": ("company", "user",)}),

    )

    list_filter = ["user name", ]


@admin.register(models.LiveWeighbridgeManage)
class LiveWeighbridgeManageAdmin(admin.ModelAdmin):
    list_display = ["name", "username", "lastname", "phone_number", "Live_Weighbridge_Manager_id", ]

    fieldsets = (

        ("personal information", {"fields": ("name", "username", "lastname",
         "phone_number", "Live_Weighbridge_Manager_id", )}),
        ("relation information", {"fields": ("company", "user",)}),

    )

    list_filter = ["user name", ]


@admin.register(models.PreColdManager)
class PreColdManagerAdmin(admin.ModelAdmin):
    list_display = ["name", "username", "lastname", "phone_number", "Pre_Cold_id", "company", "user", ]

    fieldsets = (

        ("personal information", {"fields": ("name", "username", "lastname", "phone_number", "Pre_Cold_id", )}),
        ("relation information", {"fields": ("company", "user",)}),

    )

    list_filter = ["user name", ]


@admin.register(models.ProductOwner)
class ProductOwnerAdmin(admin.ModelAdmin):
    list_display = ["name", "product_owner_id", ]

    fieldsets = (

        ("information product_owner", {"fields": ("name", "product_owner_id")}),

    )

    list_filter = ["name", ]


@admin.register(models.Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["car_number", "live_product", "car_id", "product_owner ", ]

    fieldsets = (

        ("car information", {"fields": ("car_number", "live_product", "car_id",  )}),
        ("relation information", {"fields": ("product_owner ",)}),

    )

    list_filter = ["car_id", ]


@admin.register(models.Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ["name", "last_name", "phone_number", "driver_id", "car", ]

    fieldsets = (

        ("Driver information", {"fields": ("car_number", "live_product", "car_id", )}),
        ("relation information", {"fields": ("car",)}),

    )

    list_filter = ["name", "last_name", ]


@admin.register(models.LiveWeighbridge)
class LiveWeighbridgeAdmin(admin.ModelAdmin):
    list_display = ["live_weighbridge_id", "final_weight", "car_weight", "car_empty", "weighting_date",
                    "product_category", "slaughter_status ", "slaughter_start_date", "slaughter_finish_date",
                    "buy_price", "Live_Weighbridge_Manager", "driver", ]

    fieldsets = (

        ("Time information", {"fields": ("slaughter_status ", "slaughter_start_date", "slaughter_finish_date", "weighting_date", )}),
        ("Weight information", {"fields": ("final_weight", "car_weight", "car_empty",)}),
        ("other information", {"fields": ("live_weighbridge_id", "product_category", "buy_price", )}),
        ("relation information", {"fields": ("driver ", "Live_Weighbridge_Manager")}),

    )

    list_filter = ["product_category", "final_weight", ]


@admin.register(models.FirstWeightLifting)
class FirstWeightLiftingAdmin(admin.ModelAdmin):
    list_display = ["weighting_time", "weight", "product_category", "weight_lifting_id", "sales_category",
                    "Live_Weigh_Bridge", "Weight_Lifting_Manager", ]

    fieldsets = (

        ("main information", {"fields": ("weighting_time", "weight","weight_lifting_id", )}),
        ("category information", {"fields": ("product_category", "sales_category", )}),
        ("relation information", {"fields": ("Live_Weigh_Bridge", "Weight_Lifting_Manager",)}),

    )

    list_filter = ["product_category", ]


@admin.register(models.PreCold)
class PreColdAdmin(admin.ModelAdmin):
    list_display = ["entry_time", "exit_time", "weight", "product_category", "pre_cold_id",
                    "pallet_id", "First_Weight_Lifting", "PreCold_Manager", ]

    fieldsets = (

        ("main information", {"fields": ("weight", "product_category", "pre_cold_id", "pallet_id", )}),
        ("time information", {"fields": ("entry_time", "exit_time", )}),
        ("relation information", {"fields": ("First_Weight_Lifting", "PreCold_Manager",)}),

    )

    list_filter = ["product_category", ]


@admin.register(models.Distributed)
class DistributedAdmin(admin.ModelAdmin):
    list_display = ["entry_time", "exit_time", "weight", "product_category", "pre_cold_id",
                    "pallet_id", "First_Weight_Lifting", "PreCold_Manager", ]

    fieldsets = (

        ("main information", {"fields": ("weight", "product_category", "pre_cold_id", "pallet_id", )}),
        ("time information", {"fields": ("entry_time", "exit_time", )}),
        ("relation information", {"fields": ("First_Weight_Lifting", "PreCold_Manager",)}),

    )

    list_filter = ["product_category", ]


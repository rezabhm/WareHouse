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

    list_filter = ["username", ]


@admin.register(models.SalesManager)
class SalesManagerAdmin(admin.ModelAdmin):
    list_display = ["name", "username", "lastname", "phone_number", "sales_manager_id", ]

    fieldsets = (

        ("personal information", {"fields": ("name", "username", "lastname", "phone_number", "sales_manager_id")}),
        ("relation information", {"fields": ("company", "user",)}),

    )

    list_filter = ["username", ]


@admin.register(models.WeightLiftingManager)
class WeightLiftingManagerAdmin(admin.ModelAdmin):
    list_display = ["name", "username", "lastname", "phone_number", "Weight_Lifting_Manager_id", ]

    fieldsets = (
        ("personal information", {"fields": ("name", "username", "lastname", "phone_number",
         "Weight_Lifting_Manager_id", )}),
        ("relation information", {"fields": ("company", "user",)}),
    )

    list_filter = ["username", ]


@admin.register(models.FreezingTunnelManager)
class FreezingTunnelManagerAdmin(admin.ModelAdmin):
    list_display = ["name", "username", "lastname", "phone_number", "Freezing_tunnel_Manager_id", ]

    fieldsets = (

        ("personal information", {"fields": ("name", "username", "lastname", "phone_number",
         "Freezing_tunnel_Manager_id", )}),
        ("relation information", {"fields": ("company", "user",)}),

    )

    list_filter = ["username", ]


@admin.register(models.LiveWeighbridgeManager)
class LiveWeighbridgeManagerAdmin(admin.ModelAdmin):
    list_display = ["name", "username", "lastname", "phone_number", "Live_Weighbridge_Manager_id", ]

    fieldsets = (

        ("personal information", {"fields": ("name", "username", "lastname",
         "phone_number", "Live_Weighbridge_Manager_id", )}),
        ("relation information", {"fields": ("company", "user",)}),

    )

    list_filter = ["username", ]


@admin.register(models.PreColdManager)
class PreColdManagerAdmin(admin.ModelAdmin):
    list_display = ["name", "username", "lastname", "phone_number", "Pre_Cold_id"]

    fieldsets = (

        ("personal information", {"fields": ("name", "username", "lastname", "phone_number", "Pre_Cold_id", )}),
        ("relation information", {"fields": ("company", "user",)}),

    )

    list_filter = ["username", ]


@admin.register(models.ProductOwner)
class ProductOwnerAdmin(admin.ModelAdmin):
    list_display = ["name", 'last_name', "product_owner_id", ]

    fieldsets = (

        ("information product_owner", {"fields": ("name", 'last_name', "product_owner_id")}),

    )

    list_filter = ["name", ]


@admin.register(models.Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["car_number", "live_product", "car_id", ]

    fieldsets = (

        ("car information", {"fields": ("car_number", "car_number1", "car_number2", "car_number3", "car_number4",
                                        "live_product", "car_id", )}),
        ("relation information", {"fields": ("product_owner",)}),

    )

    list_filter = ["car_id", ]


@admin.register(models.Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ["name", "last_name", "phone_number", "driver_id", ]

    fieldsets = (

        ("Driver information", {"fields": ("name", "last_name", "phone_number", "driver_id",)}),
        ("relation information", {"fields": ("car",)}),

    )

    list_filter = ["name", "last_name", ]


@admin.register(models.LiveWeighbridge)
class LiveWeighbridgeAdmin(admin.ModelAdmin):

    list_display = ["live_weighbridge_id", "final_weight", "car_weight", "car_empty", "weighting_date",
                    "product_category", "slaughter_start_date", "slaughter_finish_date",
                    "buy_price", ]

    fieldsets = (

        ("Time information", {"fields": ("slaughter_status", "slaughter_start_date", "slaughter_start_date_format",
                                         "slaughter_finish_date", "slaughter_finish_date_format", "weighting_date",
                                         "weighting_date_format"

                                         )}),
        ("Weight information", {"fields": ("final_weight", "car_weight", "car_empty", 'finish',
                                           "avicultureـcity", "avicultureـname", "order_weight", "cage_num",
                                           "product_num_in_cage", "losses_num", "losses_weight", "victim_num",
                                           "victim_weight"

                                           )}),
        ("other information", {"fields": ("live_weighbridge_id", "product_category", "buy_price", )}),
        ("relation information", {"fields": ("driver", "Live_Weighbridge_Manager", "car", "product_owner")}),

    )

    list_filter = ["product_category", "final_weight", ]


@admin.register(models.FirstWeightLifting)
class FirstWeightLiftingAdmin(admin.ModelAdmin):
    list_display = ["weighting_time", "weight", "product_category", "weight_lifting_id", "sales_category", ]

    fieldsets = (

        ("main information", {"fields": ("weighting_time", "weight", "weight_lifting_id", )}),
        ("category information", {"fields": ("product_category", "sales_category", )}),
        ("relation information", {"fields": ("Live_Weigh_Bridge", "Weight_Lifting_Manager",)}),

    )

    list_filter = ["product_category", ]

"""

@admin.register(models.PreCold)
class PreColdAdmin(admin.ModelAdmin):
    list_display = ["entry_time", "exit_time", "weight", "product_category", "pre_cold_id",
                    "pallet_id", ]

    fieldsets = (

        ("main information", {"fields": ("weight", "product_category", "pre_cold_id", "pallet_id", )}),
        ("time information", {"fields": ("entry_time", "exit_time", )}),
        ("relation information", {"fields": ("First_Weight_Lifting", "PreCold_Manager",)}),

    )

    list_filter = ["product_category", ]


@admin.register(models.Distributed)
class DistributedAdmin(admin.ModelAdmin):
    list_display = ["weight", "date", "product_category", "sale_price",
                    "bill_of_lading", "number_of_box"]

    fieldsets = (

        ("main information", {"fields": ("weight", "product_category", "date", "sale_price",
         "bill_of_lading", "number_of_box",)}),
        ("relation information", {"fields": ("first_weight_lifting", "sales_manager", "driver", )}),

    )

    list_filter = ["product_category", ]


@admin.register(models.FreezingTunnel)
class FreezingTunnelAdmin(admin.ModelAdmin):
    list_display = ["entry_date", "exit_date", "product_category", "status", ]

    fieldsets = (

        ("main information", {"fields": ("product_category", "weight", "tunnel_id", "pallet_id", "status", )}),
        ("time information", {"fields": ("entry_date", "exit_date", )}),
        ("relation information", {"fields": ("first_weight_lifting", "freezing_tunnel_manager",)}),

    )

    list_filter = ["product_category", ]


@admin.register(models.ColdHouse)
class ColdHouseAdmin(admin.ModelAdmin):
    list_display = ["entry_date", "exit_date", "pallet_status", "total_pallet_weight", ]

    fieldsets = (

        ("main information", {"fields": ("pallet_status", "total_pallet_weight", "pallet_weight_without_product",
         "number_of_box", "cold_house_id", "pallet_id", )}),
        ("time information", {"fields": ("entry_date", "exit_date", )}),
        ("relation information", {"fields": ("freezing_tunnel_manager", )}),

    )

    list_filter = ["pallet_status", ]


@admin.register(models.PaperBox)
class PaperBoxAdmin(admin.ModelAdmin):
    list_display = ["paper_box_weight", "number_of_product", "product_category", "box_id", ]

    fieldsets = (

        ("main information", {"fields": ("product_category", "paper_box_weight", "number_of_product",
         "packing_time", "box_id", )}),
        ("relation information", {"fields": ("cold_house", )}),

    )

    list_filter = ["product_category", ]

"""
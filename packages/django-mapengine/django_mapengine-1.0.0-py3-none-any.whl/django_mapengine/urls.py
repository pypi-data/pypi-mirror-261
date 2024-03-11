"""URLs for MVTs and cluster geojsons"""

from django.conf import settings
from django.urls import path
from django_distill import distill_path
from djgeojson.views import GeoJSONLayerView

from . import distill, mvt, views

app_name = "django_mapengine"

urlpatterns = [
    path("", views.index, name="index"),
]

urlpatterns += [
    path(
        f"clusters/{cluster.layer_id}.geojson",
        GeoJSONLayerView.as_view(model=cluster.model, properties=cluster.properties),
        name=f"{cluster.layer_id}_cluster",
    )
    for cluster in settings.MAP_ENGINE_API_CLUSTERS
]

urlpatterns += [
    path(
        f"{name}_mvt/<int:z>/<int:x>/<int:y>/",
        mvt.mvt_view_factory(name, [mvt.MVTLayer(mvt_api.layer_id, queryset=mvt_api.manager) for mvt_api in mvt_apis]),
    )
    for name, mvt_apis in settings.MAP_ENGINE_API_MVTS.items()
]

# Distill MVT-urls:
if settings.MAP_ENGINE_DISTILL:
    urlpatterns += [
        distill_path(
            f"<int:z>/<int:x>/<int:y>/{name}.mvt",
            mvt.mvt_view_factory(
                name, [mvt.MVTLayer(mvt_api.layer_id, queryset=mvt_api.manager) for mvt_api in mvt_apis]
            ),
            name=name,
            distill_func=distill.get_all_statics_for_state_lod,
            distill_status_codes=(200, 204, 400),
        )
        for name, mvt_apis in settings.MAP_ENGINE_API_MVTS.items()
    ]

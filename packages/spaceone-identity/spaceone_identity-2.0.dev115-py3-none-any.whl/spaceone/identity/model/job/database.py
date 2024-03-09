from mongoengine import *
from spaceone.core.model.mongo_model import MongoModel


class Job(MongoModel):
    job_id = StringField(max_length=40, generate_id="pg", unique=True)
    status = StringField(
        choices=("PENDING", "IN_PROGRESS", "FAILURE", "SUCCESS", "CANCELED"),
        default="PENDING",
    )
    resource_group = StringField(max_length=40, choices=("DOMAIN", "WORKSPACE"))
    trusted_account_id = StringField(max_length=40)
    plugin_id = StringField(max_length=40, default=None, null=True)
    workspace_id = StringField(max_length=40)
    domain_id = StringField(max_length=40)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    finished_at = DateTimeField(default=None, null=True)

    meta = {
        "updatable_fields": [
            "status",
            "updated_at",
            "finished_at",
        ],
        "minimal_fields": [
            "job_id",
            "trusted_account_id",
            "status",
            "created_at",
            "finished_at",
        ],
        "ordering": ["-created_at"],
        "indexes": [
            "plugin_id",
            "trusted_account_id",
            "workspace_id",
            "domain_id",
        ],
    }

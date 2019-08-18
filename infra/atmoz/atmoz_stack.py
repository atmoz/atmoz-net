from aws_cdk import core

from .static_site import StaticSite, StaticSiteProps


class AtmozStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        StaticSite(
            self,
            "static-site",
            StaticSiteProps(
                domain="atmoz.net",
                sub_domain="www",
                cert_arn=self.node.try_get_context("certificate-arn"),
            ),
        )

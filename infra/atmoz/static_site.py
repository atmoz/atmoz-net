from aws_cdk import (
    core,
    aws_s3,
    aws_certificatemanager,
    aws_cloudfront,
    aws_route53,
    aws_route53_targets,
)


class StaticSiteProps:
    def __init__(self, domain: str, sub_domain: str, cert_arn):
        self.domain = domain
        self.sub_domain = sub_domain
        self.full_domain = self.sub_domain + "." + self.domain
        self.cert_arn = cert_arn


class StaticSite(core.Construct):
    def __init__(self, scope: core.Construct, id: str, props: StaticSiteProps):
        super().__init__(scope, id)

        # siteDomain = props.full_domain

        bucket = aws_s3.Bucket.from_bucket_name(
            self, "bucket", bucket_name=props.domain
        )
        if not bucket:
            bucket = aws_s3.Bucket(
                self,
                "bucket",
                bucket_name=props.domain,
                website_index_document="index.html",
                website_error_document="error.html",
                public_read_access=True,
            )

        distribution = aws_cloudfront.CloudFrontWebDistribution(
            self,
            "distribution",
            alias_configuration=aws_cloudfront.AliasConfiguration(
                acm_cert_ref=props.cert_arn,
                names=[props.domain],
                ssl_method=aws_cloudfront.SSLMethod.SNI,
                security_policy=aws_cloudfront.SecurityPolicyProtocol.TLS_V1_2016,
            ),
            origin_configs=[
                aws_cloudfront.SourceConfiguration(
                    s3_origin_source=aws_cloudfront.S3OriginConfig(
                        s3_bucket_source=bucket
                    ),
                    behaviors=[aws_cloudfront.Behavior(is_default_behavior=True)],
                )
            ],
        )

        hosted_zone = aws_route53.HostedZone.from_lookup(
            self, "hosted-zone", domain_name=props.domain
        )
        if not hosted_zone:
            hosted_zone = aws_route53.HostedZone(
                self, "hosted-zone", zone_name=props.domain
            )

        aws_route53.ARecord(
            self,
            "record",
            record_name=props.domain,
            target=aws_route53.AddressRecordTarget.from_alias(
                aws_route53_targets.CloudFrontTarget(distribution)
            ),
            zone=hosted_zone,
        )

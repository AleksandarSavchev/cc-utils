import gci.componentmodel as cm

import cnudie.retrieve
import cnudie.iter
import ctx


_cfg = ctx.cfg


def traverse(
    name: str,
    version: str=None,
    ctx_base_url: str=None,
    components: bool=True,
    sources: bool=True,
    resources: bool=True,
):
    if not ctx_base_url:
        ctx_base_url = _cfg.ctx.ocm_repo_base_url

    if not version:
        name, version = name.rsplit(':', 1)

    ctx_repo = cm.OciRepositoryContext(
        baseUrl=ctx_base_url,
    )

    component_descriptor_lookup = cnudie.retrieve.create_default_component_descriptor_lookup(
        default_ctx_repo=ctx_repo,
    )

    component_descriptor = component_descriptor_lookup(cm.ComponentIdentity(
        name=name,
        version=version,
    ))
    component = component_descriptor.component

    for node in cnudie.iter.iter(
        component=component,
        lookup=component_descriptor_lookup,
    ):
        indent = len(node.path * 2)
        if isinstance(node, cnudie.iter.ComponentNode):
            if not components:
                continue
            prefix = 'c'
            print(f'{prefix}{" " * indent}{node.component.name}:{node.component.version}')
        if isinstance(node, cnudie.iter.ResourceNode):
            if not resources:
                continue
            prefix = 'r'
            indent += 1
            print(f'{prefix}{" " * indent}{node.resource.name}')
        if isinstance(node, cnudie.iter.SourceNode):
            if not sources:
                continue
            prefix = 'r'
            indent += 1
            print(f'{prefix}{" " * indent}{node.source.name}')

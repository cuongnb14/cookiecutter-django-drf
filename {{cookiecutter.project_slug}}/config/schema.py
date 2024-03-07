def custom_postprocessing_hook(result, generator, request, public):
    for path, value in result['paths'].items():
        for method, ops in value.items():
            if 'summary' not in ops:
                pieces = ops['operationId'].split('_')
                ops['summary'] = f'{pieces[-1]} {" ".join(pieces[:-1])}'
    return result

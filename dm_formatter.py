# Convert drexel_metadata JSON file to BGNN minnow metadata JSON file
import json
import argparse


def reformat_for_bgnn(result):
    """
    Reformat and reduce the size of the result dictionary. 
    Collect only the data necessary for BGNN minnow project. The new format matches the 
    BGNN_metadata version. Therefore some of the value not calcualted in drexel version are by 
    defaulset to "None". 

    Parameters
    ----------
    result : dict
        DESCRIPTION. output from gen_metadata()

    Returns
    -------
    bgnn_result : dict
        DESCRIPTION. {'base_name': xx, 'version':xx, 
                       'fish': {'fish_num': xx,"bbox":xx, 'pixel_analysis':xx, 'rescale':xx, 
                            'eye_bbox': xx, 'eye_center':xx , 'angle_degree': xx,
                            'eye_direction':xx, 'foreground_mean':xx, 'background_mean':xx}, 
                       'ruler': {'bbox':xx, 'scale':xx, 'unit':xx}}

    """
    
    name_base = list(result.keys())[0]
    first_value = list(result.values())[0]
    
    # Fish metadata
    fish_num = first_value['fish_count']
    fish_bbox = first_value['fish'][0]['bbox']
    pixel_analysis = False if first_value['fish'][0]['pixel_analysis_failed'] else True
    
    if first_value['fish'][0]['has_eye']:
        eye_center = first_value['fish'][0]['eye_center']
    else :
        eye_center = "None"
    
    eye_direction = first_value['fish'][0]['side']
    foreground_mean = first_value['fish'][0]['foreground']['mean']
    background_mean = first_value['fish'][0]['background']['mean']
        
    dict_fish = {'fish_num': fish_num,"bbox":fish_bbox, 
                 'pixel_analysis':pixel_analysis, 'rescale':"None", 
                 'eye_bbox': "None", 'eye_center':eye_center , 'angle_degree': "None",
                 'eye_direction':eye_direction, 'foreground_mean':round(foreground_mean,2), 
                 'background_mean':round(background_mean,2)}
    
    # Ruler metadata
    ruler_bbox  = first_value['ruler_bbox'] if first_value['has_ruler'] else "None"
    scale = round(first_value['scale'],2) if "scale" in first_value.keys() else "None"
    unit = first_value['unit'] if "unit" in first_value.keys() else "None"
    
    dict_ruler = {'bbox':ruler_bbox, 'scale':scale, 'unit':unit}
    
    bgnn_result = {'base_name': name_base, 'version':"from drexel", 
                   'fish': dict_fish, 'ruler': dict_ruler} 
    
    return bgnn_result


def argument_parser():
    parser = argparse.ArgumentParser(description='Convert metadata json file to BGNN minnow project format.')
    parser.add_argument('input', help='Path of input drexel_metadata format JSON metadata file.')
    parser.add_argument('output', help='Path of output BGNN minnow format JSON metadata file.')
    return parser


def main():
    parser = argument_parser()
    args = parser.parse_args()
    print(f"Converting {args.input} to BGNN minnows format {args.output}")
    with open(args.input, 'r') as infile:
        data = json.load(infile)
        result = reformat_for_bgnn(data)
        with open(args.output, 'w') as outfile:
             outfile.write(json.dumps(result))


if __name__ == '__main__':
    main()

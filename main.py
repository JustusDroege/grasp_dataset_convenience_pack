from .data import DataSet, Options, enums

"""
Example usage.
"""
if __name__ == '__main__':
    # load data:
    data = DataSet.Dataset("/path/to/data")

    #visualize with plt
    data.subfolders[0].datapoints[0].visualize()

    #save to location
    data.subfolders[0].datapoints[0].save("/home/path/to/save/to", "filename_without_extension")

    #change options
    options = Options.Options(
                    visiualization_option=enums.visiualization_option.RANDOM,
                    save_option=enums.save_option.RANDOM,
                    amount=5,
                    indices=[1],
                    circle_radius=2,
                    line_thickness=2,
                    circle_colors=[(100,255,255), (255,255,100), (255,100,255), (100,100,100)], 
                    line_colors=[(100,255,0), (0,255,100)]
            )

    #pass options to vis/save:
    data.subfolders[1].datapoints[1].visualize(options)
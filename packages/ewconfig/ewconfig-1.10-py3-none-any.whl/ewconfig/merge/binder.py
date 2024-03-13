from glob import glob
from logging import getLogger
import os

import numpy as np
from obspy import read_inventory
import obspy.geodetics.base as geodetics

from ewconfig.pz.xml import XmlPolesZeros, UnsupportedResponseException
# Import the module to avoid circular import errors.
import ewconfig.lib.write as write

log = getLogger(__name__)


def compute_grid_limits(lon, lat, border_win_ratio = 0.25,
                        min_border = 0.1, max_border = 10,
                        round_dec = 2):
    ''' Compute the binder grid limits from station coordinates.
    
    Parameters
    ---------.
    lon: :obj:`list` of float
        The station longitude values.
        
    lat: :obj:`list` of float
        The station latitude values.
        
    border_win_ratio: float
        The ratio of the total extent used to add a border
        to the grid (0 -1)
        
    min_border: float
        The minimum border width [degree].
        
    max_border: float
        The maximum border width [degree].

    round_dec: None or int
        Round to these number of decimals.
        If None, the values are not rounded.
        
    Returns
    -------
    :obj:`list` of float (2x2)
        The grid limits.
        [[lon_min, lon_max],
         [lat_min, lat_max]
    '''
    # Get the coordinate limits.
    min_lat = min(lat)
    max_lat = max(lat)
    min_lon = min(lon)
    max_lon = max(lon)

    # Compute the border width.
    border_lat = (max_lat - min_lat) * border_win_ratio
    border_lon = (max_lon - min_lon) * border_win_ratio

    if border_lat < min_border:
        border_lat = min_border

    if border_lat > max_border:
        border_lat = max_border

    if border_lon < min_border:
        border_lon = min_border

    if border_lon > max_border:
        border_lon = max_border

    # Add the border.
    grid_limits = [min_lat - border_lat,
                   max_lat + border_lat,
                   min_lon - border_lon,
                   max_lon + border_lon]

    # Check coordinate limits.
    if (grid_limits[0] < -90):
        grid_limits[0] = -90

    if(grid_limits[1] > 90):
        grid_limits[1] = 90

    if(grid_limits[2] < -180):
        grid_limits[2] = -180

    if(grid_limits[3] > 180):
        grid_limits[3] = 180

    if round_dec is not None:
        grid_limits = [round(x, round_dec) for x in grid_limits]
 
    return grid_limits


def compute_grid_parameters(lon, lat):
    ''' Compute the binder grid parameters.

    Parameters
    ---------.
    lon: :obj:`list` of float
        The station longitude values.
  
    lat: :obj:`list` of float
        The station latitude values.

    Returns
    -------
    :obj:`dictionary`
        The computed grid parameters with the parameter names as keys.
    '''
    ret = {}
    ret['dspace'] = 4.0
    ret['rstack'] = 100.0
    ret['tstack'] = 0.5
    stat_coords = np.array(list(zip(lon, lat)))
    stat_coords = np.unique(stat_coords, axis = 0)

    n_stations = len(stat_coords)

    # Return the default values if less than 2 stations
    # are passed.
    if n_stations <= 1:
        return ret

    dist = []
    for k in range(n_stations - 1):
        cur_main = stat_coords[k, :]
        for m in range(k + 1, n_stations):
            cur_ref = stat_coords[m, :]
            cur_dist = geodetics.gps2dist_azimuth(cur_main[1], cur_main[0],
                                                  cur_ref[1], cur_ref[0])
            dist.append(cur_dist[0])
    dist = np.array(dist)

    #log.info('#### Computing grid parameters.')
    #log.info('#### dist: {}.'.format(dist))
    #log.info('#### n_stations: {}.'.format(n_stations))
    #log.info('#### stat_coords: {}.'.format(stat_coords))
    
    # Compute the binder parameters.
    # dspace
    ratio = 0.25
    min_dist = np.min(dist)
    dspace = np.floor((min_dist * ratio) / 1000) * 1000

    # rstack
    factor = 0.75
    med_dist = np.median(dist)
    rstack = (med_dist - (med_dist % dspace)) * factor

    # tstack
    # As a first approximation, tstack should be at least the number
    # of seconds it takes for a P-wave to cross a grid cell of dspace km.
    # Compute the traveltime using a constant vp velocity.
    ncells = 2
    vp = 4000
    tstack = (dspace * ncells) / vp

    ret = {}
    ret['dspace'] = dspace / 1000
    ret['rstack'] = rstack / 1000
    ret['tstack'] = tstack

    return ret


def compute_binder_grid(old, subdir='stationxml'):
    ''' Compute the binder grid using stationXML files.
    '''
    def xml_files_in(dir):
        search_path = os.path.join(dir, '**', '*.xml')
        yield from (file for file in glob(search_path, recursive = True))
        
    xml_path = os.path.join(old, subdir)

    # Read all available station XML files of the merged directory.
    inv = None
    for file in xml_files_in(xml_path):
        cur_inv = read_inventory(file)
        if inv is None:
            inv = cur_inv
        else:
            inv.extend(cur_inv)

    if not inv:
        log.warning(f'No station XML files in {xml_path}')
    else:
        # Compute the grid limits.
        sncls = []
        for cur_net in inv:
            for cur_stat in cur_net:
                for cur_chan in cur_stat:
                    try:
                        cur_pz = XmlPolesZeros(cur_net, cur_stat, cur_chan,
                                               lo_precision=False,
                                               default_response=None)
                        sncls.append(cur_pz)
                    except UnsupportedResponseException:
                        log.warning(f'Skipping {cur_stat}.{cur_net}.{cur_chan} (pressure sensitive detector)')

        eqk_dir = os.path.join(old, 'eqk')
        write.write_binder_grid(eqk_dir, sncls)
    

    

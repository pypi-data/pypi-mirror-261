import click
import numpy as np
from datetime import datetime

@click.group()
def nmr():
    pass



@click.command()
@click.option("--b", help="Byte order", default=0)
@click.option("--input", prompt="Input folder location", help="Input folder", type=click.Path(exists=True))
@click.option("--output", prompt="Output folder location", help="Output folder")
@click.option("--npi", type=int, prompt="Numer of points in indirect dimension", help="Number of points in indirect dimension")
@click.option("--npd", type=int, prompt="Number of points in direct dimension", help="Number of points in direct dimension")

def ser2np(input, output, npi, npd, b):
    input = input.replace('\\', '/')
    output = output.replace('\\', '/')

    if b == 0:
        dtype = '<i4'
    elif b == 1:
        dtype = '>i4'

    input_file = input + '/ser'

    with open(input_file, 'rb') as input_serial_file: 
        raw_data = np.frombuffer(input_serial_file.read(), dtype=dtype)
    data_length = len(raw_data)  
    if data_length != int(npi * npd):
        print("Data length mismatch! Please check the parameters. Exiting...")
        exit()       

    fid2d = []
    for i  in range(npi):
        a = i * npd
        b = (i+1) * npd
        fid_data = raw_data[a:b] 
        reals = fid_data[0::2]    
        imags = fid_data[1::2] 
        fid = reals + 1.j*imags
        fid2d.append(fid)

    fid2d = np.array(fid2d) # numpy array of all the FIDs (256, 2048). Real and imaginary parts are mixed.
    date = datetime.now().strftime("%M%S")
    dt = 'fid2d_' + date + '_' + str(npi) + '_' + str(npd) +'.npy'
    if output == '':
        output_file = dt
    else:
        output_file = output + '/' + dt
    np.save(output_file, fid2d)
    print(f"File saved as : {dt}")


@click.command()
@click.option("--input", prompt="Location of numpy file", help="Location of numpy file",type=click.Path(exists=True))
@click.option("--output", help="Location of output folder", default='', type=click.Path(exists=False))
@click.option("--b", help="Byte order", default=0)
def np2ser (input, output, b):

    if b == 0:
        dtype = '<i4'
    elif b == 1:
        dtype = '>i4'
    fid_chunks = []
    fid2d = np.load(input)
    for fid in fid2d:
        reals = np.real(fid)
        imags = np.imag(fid)

        fid_chunk = np.column_stack((reals, imags)).flatten()
        fid_chunks.append(fid_chunk)
    raw_data_reconstructed = np.concatenate(fid_chunks)
    dt = datetime.now().strftime("%M%S")
    if output == '':
        output_file = 'ser_' + dt
    else:
        output_file = output + '/ser_' + dt

    with open(output_file, 'wb') as output_serial_file: 
        output_serial_file.write(np.array(raw_data_reconstructed, dtype=dtype).tobytes())
    print(f"File saved as : {output_file}")

nmr.add_command(ser2np)
nmr.add_command(np2ser)


if __name__ == '__main__':
    nmr()

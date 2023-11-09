from paths import main_path
import sys
sys.path.append(main_path)


from include.focus import sharp

def main() -> None:
    # Try out the sharp function by comparing image 20 and REF_23
    sharp(20)
    
if __name__ == '__main__':
    main()
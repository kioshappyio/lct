import random
import time
from rich.console import Console
from rich.progress import Progress
from colorama import Fore, Style, init

# Inisialisasi colorama
init(autoreset=True)

# Konsol untuk menampilkan teks berwarna dan terstruktur
console = Console()

# Fungsi untuk menghasilkan koordinat lokasi acak yang realistis
def generate_random_location(seed):
    lat_min = -8
    lat_max = -5
    lon_min = 95
    lon_max = 141
    lat = lat_min + (lat_max - lat_min) * seed
    lon = lon_min + (lon_max - lon_min) * seed
    return f"{lat:.6f}, {lon:.6f}"

# Fungsi untuk memilih kota dan daerah acak yang lebih relevan
def generate_random_location_details():
    cities = [
        "Jakarta", "Bandung", "Surabaya", "Medan", "Makassar", 
        "Yogyakarta", "Bali", "Semarang", "Malang", "Palembang", 
        "Solo", "Balikpapan", "Batam", "Denpasar", "Ambon", 
        "Cirebon", "Manado", "Pontianak", "Banjarmasin", "Pekanbaru", 
        "Lampung", "Samarinda", "Mataram", "Jambi", "Tangerang"
    ]
    regions = [
        "Pusat", "Utara", "Timur", "Selatan", "Barat", 
        "Tengah", "Pantai", "Gunung", "Laut", "Padang", 
        "Hutan", "Perbatasan", "Industri", "Perkotaan", "Pedesaan", 
        "Teluk", "Lembah", "Dataran", "Delta", "Pesisir"
    ]

    random_city = random.choice(cities)
    random_region = random.choice(regions)
    return f"{random_city}, {random_region}"

# Fungsi untuk mencetak proses palsu dengan animasi
def fake_tracking_process():
    console.print("[yellow]Mengakses server lokasi...[/yellow]")
    with Progress() as progress:
        task = progress.add_task("[cyan]Menghubungkan...[/cyan]", total=100)
        while not progress.finished:
            progress.update(task, advance=10)
            time.sleep(0.3)
    console.print("[green]Selesai mengakses server lokasi![/green]")

    time.sleep(1)
    console.print("[yellow]Menganalisis nomor telepon...[/yellow]")
    time.sleep(2)

    console.print("[yellow]Menemukan lokasi pengguna...[/yellow]")
    time.sleep(2)

    console.print("[yellow]Memverifikasi data lokasi...[/yellow]")
    time.sleep(1)

# Meminta nomor telepon sekali di awal
console.print("[bold green]Selamat datang di Sistem Pelacakan Lokasi.[/bold green]")
phone_number = input(Fore.CYAN + "Masukkan nomor telepon: ")
console.print(f"[cyan]Melacak lokasi untuk nomor telepon: [bold]{phone_number}[/bold][/cyan]\n")

# Perulangan untuk melacak lokasi tanpa meminta input lagi
while True:
    fake_tracking_process()

    # Hasilkan data palsu yang lebih realistis
    coordinates = generate_random_location(sum([ord(c) for c in phone_number]) / len(phone_number))
    location_details = generate_random_location_details()
    fake_ip = f"192.168.{random.randint(0, 255)}.{random.randint(0, 255)}"

    # Tampilkan hasil dengan warna
    console.print("[bold green]Data ditemukan:[/bold green]")
    time.sleep(1)
    console.print(f"[bold blue]- Kota      :[/bold blue] [cyan]{location_details.split(',')[0]}[/cyan]")
    console.print(f"[bold blue]- Daerah    :[/bold blue] [cyan]{location_details.split(',')[1]}[/cyan]")
    console.print(f"[bold blue]- Koordinat :[/bold blue] [cyan]{coordinates}[/cyan]")
    console.print(f"[bold blue]- IP        :[/bold blue] [cyan]{fake_ip}[/cyan]\n")
    time.sleep(2)

    # Hasil akhir
    console.print("[yellow]Memvalidasi data lokasi...[/yellow]")
    time.sleep(2)
    console.print("[red bold]Error: Lokasi tidak dapat ditemukan.[/red bold]\n")
    time.sleep(1)

    # Simpan hasil ke file log
    log_file = "tracking_log.txt"
    with open(log_file, "a") as f:
        f.write(f"Nomor: {phone_number}\n")
        f.write(f"Kota: {location_details.split(',')[0]}\n")
        f.write(f"Daerah: {location_details.split(',')[1]}\n")
        f.write(f"Koordinat: {coordinates}\n")
        f.write(f"IP: {fake_ip}\n")
        f.write("Status: Tidak ditemukan\n")
        f.write("---\n")

    console.print(f"[green]Hasil telah disimpan di [bold]{log_file}[/bold][/green]")
    console.print("[cyan]Melacak kembali...\n[/cyan]")
    time.sleep(3)

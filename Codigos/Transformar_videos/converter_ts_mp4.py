import os
import subprocess
import sys
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

def encontrar_ffmpeg():
    """Encontra o executável do FFmpeg no sistema ou localmente"""
    # Atualiza o PATH do processo atual com as variáveis do sistema
    import os
    system_path = os.environ.get("Path", "")
    machine_path = os.environ.get("Path", "")
    try:
        import winreg
        # Tenta pegar o PATH da máquina
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment") as key:
            machine_path = winreg.QueryValueEx(key, "Path")[0]
    except:
        pass
    
    # Atualiza PATH temporariamente
    os.environ["Path"] = machine_path + ";" + os.environ.get("Path", "")
    
    # Primeiro tenta no PATH
    try:
        subprocess.run(['ffmpeg', '-version'], capture_output=True, check=True, timeout=5)
        return 'ffmpeg'
    except (FileNotFoundError, subprocess.CalledProcessError, subprocess.TimeoutExpired):
        pass
    
    # Procura localmente na pasta ffmpeg
    ffmpeg_dir = Path(__file__).parent / "ffmpeg"
    if ffmpeg_dir.exists():
        for bin_dir in ffmpeg_dir.glob("*/bin"):
            ffmpeg_exe = bin_dir / "ffmpeg.exe"
            if ffmpeg_exe.exists():
                try:
                    subprocess.run([str(ffmpeg_exe), '-version'], capture_output=True, check=True)
                    return str(ffmpeg_exe)
                except:
                    pass
    
    # Procura no local de instalação do WinGet
    winget_packages = Path(os.environ.get("LOCALAPPDATA", "")) / "Microsoft" / "WinGet" / "Packages"
    if winget_packages.exists():
        # Procura por pastas do FFmpeg instaladas via WinGet
        for ffmpeg_folder in winget_packages.glob("*FFmpeg*"):
            # Procura em subpastas por ffmpeg.exe
            for ffmpeg_exe in ffmpeg_folder.rglob("ffmpeg.exe"):
                if ffmpeg_exe.exists():
                    try:
                        subprocess.run([str(ffmpeg_exe), '-version'], capture_output=True, check=True)
                        return str(ffmpeg_exe)
                    except:
                        pass
    
    # Procura em locais comuns do Windows
    locais_comuns = [
        Path("C:/ffmpeg/bin/ffmpeg.exe"),
        Path("C:/Program Files/ffmpeg/bin/ffmpeg.exe"),
        Path(os.environ.get("ProgramFiles", "")) / "ffmpeg/bin/ffmpeg.exe",
    ]
    
    for local in locais_comuns:
        if local.exists():
            try:
                subprocess.run([str(local), '-version'], capture_output=True, check=True)
                return str(local)
            except:
                pass
    
    return None

class ConversorTS:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor TS para MP4")
        self.root.geometry("650x550")
        self.root.minsize(600, 500)
        
        # Lista de arquivos selecionados
        self.arquivos_ts = []
        
        # Caminho do FFmpeg
        self.ffmpeg_path = encontrar_ffmpeg()
        
        # Interface
        self.criar_interface()
    
    def criar_interface(self):
        # Canvas com scrollbar para garantir que tudo seja visível
        canvas = tk.Canvas(self.root)
        scrollbar_principal = ttk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar_principal.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar_principal.pack(side="right", fill="y")
        
        # Frame principal
        frame_principal = ttk.Frame(scrollable_frame, padding="10")
        frame_principal.pack(fill=tk.BOTH, expand=True)
        
        # Título
        titulo = ttk.Label(
            frame_principal, 
            text="Conversor TS para MP4", 
            font=("Arial", 16, "bold")
        )
        titulo.pack(pady=10)
        
        # Botão para selecionar arquivos
        btn_selecionar = ttk.Button(
            frame_principal,
            text="📁 Selecionar Vídeos TS",
            command=self.selecionar_arquivos,
            width=30
        )
        btn_selecionar.pack(pady=10)
        
        # Lista de arquivos selecionados
        frame_lista = ttk.Frame(frame_principal)
        frame_lista.pack(fill=tk.BOTH, expand=True, pady=10)
        
        ttk.Label(frame_lista, text="Arquivos selecionados:", font=("Arial", 10, "bold")).pack(anchor=tk.W)
        
        # Scrollbar e Listbox
        scrollbar = ttk.Scrollbar(frame_lista)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.lista_arquivos = tk.Listbox(
            frame_lista,
            yscrollcommand=scrollbar.set,
            height=8
        )
        self.lista_arquivos.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.lista_arquivos.yview)
        
        # Botão para remover selecionado
        btn_remover = ttk.Button(
            frame_principal,
            text="Remover Selecionado",
            command=self.remover_arquivo,
            width=20
        )
        btn_remover.pack(pady=5)
        
        # Frame de opções
        frame_opcoes = ttk.LabelFrame(frame_principal, text="Opções", padding="10")
        frame_opcoes.pack(fill=tk.X, pady=10)
        
        # Pasta de saída
        ttk.Label(frame_opcoes, text="Pasta de saída (opcional):").pack(anchor=tk.W)
        frame_saida = ttk.Frame(frame_opcoes)
        frame_saida.pack(fill=tk.X, pady=5)
        
        self.entry_saida = ttk.Entry(frame_saida, width=50)
        self.entry_saida.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        
        btn_pasta = ttk.Button(
            frame_saida,
            text="📂 Escolher",
            command=self.escolher_pasta_saida,
            width=15
        )
        btn_pasta.pack(side=tk.RIGHT)
        
        # Barra de progresso
        self.progresso = ttk.Progressbar(
            frame_principal,
            mode='determinate'
        )
        self.progresso.pack(fill=tk.X, pady=10)
        
        self.label_status = ttk.Label(frame_principal, text="Pronto para converter")
        self.label_status.pack()
        
        # Botão converter (grande e destacado)
        btn_converter = ttk.Button(
            frame_principal,
            text="▶️ CONVERTER PARA MP4",
            command=self.converter_arquivos,
            width=35
        )
        btn_converter.pack(pady=20)
        
        # Bind do mouse wheel ao canvas
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
    
    def selecionar_arquivos(self):
        """Abre diálogo para selecionar múltiplos arquivos TS"""
        arquivos = filedialog.askopenfilenames(
            title="Selecione os vídeos TS",
            filetypes=[
                ("Arquivos TS", "*.ts"),
                ("Todos os arquivos", "*.*")
            ]
        )
        
        if arquivos:
            for arquivo in arquivos:
                if arquivo not in self.arquivos_ts:
                    self.arquivos_ts.append(arquivo)
                    self.lista_arquivos.insert(tk.END, os.path.basename(arquivo))
    
    def remover_arquivo(self):
        """Remove arquivo selecionado da lista"""
        selecionado = self.lista_arquivos.curselection()
        if selecionado:
            indice = selecionado[0]
            self.lista_arquivos.delete(indice)
            self.arquivos_ts.pop(indice)
    
    def escolher_pasta_saida(self):
        """Abre diálogo para escolher pasta de saída"""
        pasta = filedialog.askdirectory(title="Escolha a pasta de saída")
        if pasta:
            self.entry_saida.delete(0, tk.END)
            self.entry_saida.insert(0, pasta)
    
    def converter_arquivo(self, arquivo_ts, pasta_saida=None):
        """Converte um arquivo TS para MP4"""
        arquivo_ts = Path(arquivo_ts)
        
        if not arquivo_ts.exists():
            return False, f"Arquivo não encontrado: {arquivo_ts}"
        
        # Define o nome do arquivo de saída
        if pasta_saida:
            pasta_saida = Path(pasta_saida)
            pasta_saida.mkdir(parents=True, exist_ok=True)
            arquivo_mp4 = pasta_saida / f"{arquivo_ts.stem}.mp4"
        else:
            arquivo_mp4 = arquivo_ts.parent / f"{arquivo_ts.stem}.mp4"
        
        # Comando FFmpeg
        ffmpeg_cmd = self.ffmpeg_path if self.ffmpeg_path else 'ffmpeg'
        comando = [
            ffmpeg_cmd,
            '-i', str(arquivo_ts),
            '-c:v', 'libx264',
            '-c:a', 'aac',
            '-preset', 'medium',
            '-crf', '23',
            '-y',
            str(arquivo_mp4)
        ]
        
        try:
            resultado = subprocess.run(
                comando,
                capture_output=True,
                text=True,
                check=True
            )
            return True, f"✓ {arquivo_ts.name} → {arquivo_mp4.name}"
        except subprocess.CalledProcessError as e:
            return False, f"Erro: {arquivo_ts.name} - {e.stderr[:100]}"
        except FileNotFoundError:
            return False, "FFmpeg não encontrado. Instale FFmpeg e adicione ao PATH."
    
    def converter_arquivos(self):
        """Converte todos os arquivos selecionados"""
        if not self.arquivos_ts:
            messagebox.showwarning("Aviso", "Nenhum arquivo selecionado!")
            return
        
        # Verifica se FFmpeg está disponível
        if not self.ffmpeg_path:
            self.ffmpeg_path = encontrar_ffmpeg()
        
        if not self.ffmpeg_path:
            resposta = messagebox.askyesno(
                "FFmpeg não encontrado",
                "FFmpeg não foi encontrado no sistema.\n\n"
                "Deseja instalar automaticamente agora?\n\n"
                "(Caso contrário, você precisará instalar manualmente)"
            )
            if resposta:
                # Tenta executar o instalador
                instalador = Path(__file__).parent / "instalar_ffmpeg.py"
                if instalador.exists():
                    try:
                        subprocess.run([sys.executable, str(instalador)], check=True)
                        self.ffmpeg_path = encontrar_ffmpeg()
                        if not self.ffmpeg_path:
                            messagebox.showerror(
                                "Erro",
                                "Instalação não concluída. Por favor, instale manualmente."
                            )
                            return
                    except Exception as e:
                        messagebox.showerror(
                            "Erro",
                            f"Erro ao instalar FFmpeg: {e}\n\n"
                            "Por favor, instale manualmente."
                        )
                        return
                else:
                    messagebox.showerror(
                        "Erro",
                        "Instalador não encontrado.\n\n"
                        "Por favor, instale FFmpeg manualmente:\n"
                        "https://ffmpeg.org/download.html"
                    )
                    return
            else:
                return
        
        # Pasta de saída
        pasta_saida = self.entry_saida.get().strip() if self.entry_saida.get().strip() else None
        
        # Confirmação
        resposta = messagebox.askyesno(
            "Confirmar",
            f"Converter {len(self.arquivos_ts)} arquivo(s) TS para MP4?\n\n"
            f"Pasta de saída: {pasta_saida if pasta_saida else 'Mesma pasta dos arquivos'}"
        )
        
        if not resposta:
            return
        
        # Desabilita botões durante conversão
        self.root.update()
        
        # Configura barra de progresso
        self.progresso['maximum'] = len(self.arquivos_ts)
        self.progresso['value'] = 0
        
        sucessos = 0
        erros = []
        
        # Converte cada arquivo
        for i, arquivo_ts in enumerate(self.arquivos_ts):
            self.label_status.config(text=f"Convertendo {i+1}/{len(self.arquivos_ts)}: {os.path.basename(arquivo_ts)}")
            self.root.update()
            
            sucesso, mensagem = self.converter_arquivo(arquivo_ts, pasta_saida)
            
            if sucesso:
                sucessos += 1
            else:
                erros.append(mensagem)
            
            self.progresso['value'] = i + 1
            self.root.update()
        
        # Mostra resultado
        self.label_status.config(text=f"Concluído: {sucessos}/{len(self.arquivos_ts)} convertido(s)")
        
        mensagem_resultado = f"Conversão concluída!\n\nSucessos: {sucessos}\nErros: {len(erros)}"
        if erros:
            mensagem_resultado += f"\n\nErros:\n" + "\n".join(erros[:5])
            if len(erros) > 5:
                mensagem_resultado += f"\n... e mais {len(erros) - 5} erro(s)"
        
        messagebox.showinfo("Concluído", mensagem_resultado)

def main():
    root = tk.Tk()
    app = ConversorTS(root)
    root.mainloop()

if __name__ == "__main__":
    main()


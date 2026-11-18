; v1.0 shredder: TMNTSF.exe changes
; Generated from the released patch by gen_source.py, then checked: build.py assembles this file
; back onto the original TMNTSF.exe and must reproduce the released exe byte for byte.

size 24846848

; ---- PE header, section table and other non-code bytes
file 0x16e 09
file 0x1b9 108701000400003b94
file 0x211 0000000000
file 0x278 009e
file 0x2c8 0040
file 0x3b0 2e736872656400000030000000e086010030000000f27a01000000000000000000000000200000e0

; ---- changed instructions inside the original game code

org 0x1400d352a
    lea rcx, [rip + 0x15dcbaf]                                   ; 1400d352a  -> 0x1416b00e0
    call 0x140534f30                                             ; 1400d3531  -> 0x140534f30 std::string assign
    nop                                                          ; 1400d3536
    .bytes 33f6                                                 ; 1400d3537  xor esi, esi  (exact original encoding)
    mov qword ptr [rip + 0x15dcbc0], rsi                         ; 1400d3539  -> 0x1416b0100
    mov qword ptr [rip + 0x15dcbc9], rsi                         ; 1400d3540  -> 0x1416b0110
    lea edi, [rsi + 0xf]                                         ; 1400d3547
    mov qword ptr [rip + 0x15dcbc7], rdi                         ; 1400d354a  -> 0x1416b0118
    mov byte ptr [rip + 0x15dcba8], sil                          ; 1400d3551  -> 0x1416b0100
    lea r9, [rip + 0x107a6f1]                                    ; 1400d3558  -> 0x14114dc50 'SelectorPortrait_0/Lit'
    lea edx, [rsi + 0x16]                                        ; 1400d355f
    lea rcx, [rip + 0x15dcb97]                                   ; 1400d3562  -> 0x1416b0100
    call 0x140534f30                                             ; 1400d3569  -> 0x140534f30 std::string assign
    nop                                                          ; 1400d356e
    mov qword ptr [rip + 0x15dcbaa], rsi                         ; 1400d356f  -> 0x1416b0120
    mov qword ptr [rip + 0x15dcbb3], rsi                         ; 1400d3576  -> 0x1416b0130
    mov qword ptr [rip + 0x15dcbb4], rdi                         ; 1400d357d  -> 0x1416b0138
    mov byte ptr [rip + 0x15dcb95], sil                          ; 1400d3584  -> 0x1416b0120
    lea r9, [rip + 0x107a6a6]                                    ; 1400d358b  -> 0x14114dc38 'SelectorPortrait_0/Used'
    lea edx, [rsi + 0x17]                                        ; 1400d3592
    lea rcx, [rip + 0x15dcb84]                                   ; 1400d3595  -> 0x1416b0120
    call 0x140534f30                                             ; 1400d359c  -> 0x140534f30 std::string assign
    nop                                                          ; 1400d35a1
    mov qword ptr [rip + 0x15dcb97], rsi                         ; 1400d35a2  -> 0x1416b0140
    mov qword ptr [rip + 0x15dcba0], rsi                         ; 1400d35a9  -> 0x1416b0150
    mov qword ptr [rip + 0x15dcba1], rdi                         ; 1400d35b0  -> 0x1416b0158
    mov byte ptr [rip + 0x15dcb82], sil                          ; 1400d35b7  -> 0x1416b0140
    lea r9, [rip + 0x107a51b]                                    ; 1400d35be  -> 0x14114dae0 'SelectorPortrait_0/Locked'
    lea edx, [rsi + 0x19]                                        ; 1400d35c5
    lea rcx, [rip + 0x15dcb71]                                   ; 1400d35c8  -> 0x1416b0140
    call 0x140534f30                                             ; 1400d35cf  -> 0x140534f30 std::string assign
    nop                                                          ; 1400d35d4
    mov qword ptr [rip + 0x15dcb84], rsi                         ; 1400d35d5  -> 0x1416b0160
    mov qword ptr [rip + 0x15dcb8d], rsi                         ; 1400d35dc  -> 0x1416b0170
    mov qword ptr [rip + 0x15dcb8e], rdi                         ; 1400d35e3  -> 0x1416b0178
    mov byte ptr [rip + 0x15dcb6f], sil                          ; 1400d35ea  -> 0x1416b0160
    lea r9, [rip + 0x107a4c8]                                    ; 1400d35f1  -> 0x14114dac0 'SelectorPortrait_0/Image'
    lea edx, [rsi + 0x18]                                        ; 1400d35f8
    lea rcx, [rip + 0x15dcb5e]                                   ; 1400d35fb  -> 0x1416b0160
    call 0x140534f30                                             ; 1400d3602  -> 0x140534f30 std::string assign
    nop                                                          ; 1400d3607
    mov qword ptr [rip + 0x15dcb71], rsi                         ; 1400d3608  -> 0x1416b0180
    mov qword ptr [rip + 0x15dcb7a], rsi                         ; 1400d360f  -> 0x1416b0190
    mov qword ptr [rip + 0x15dcb7b], rdi                         ; 1400d3616  -> 0x1416b0198
    mov byte ptr [rip + 0x15dcb5c], sil                          ; 1400d361d  -> 0x1416b0180
    lea r9, [rip + 0x107a4ed]                                    ; 1400d3624  -> 0x14114db18 'SelectorPortrait_0/HeroColor'
    lea edx, [rsi + 0x1c]                                        ; 1400d362b
    lea rcx, [rip + 0x15dcb4b]                                   ; 1400d362e  -> 0x1416b0180
    call 0x140534f30                                             ; 1400d3635  -> 0x140534f30 std::string assign
    nop                                                          ; 1400d363a
    mov qword ptr [rip + 0x15dcb5e], rsi                         ; 1400d363b  -> 0x1416b01a0
    mov qword ptr [rip + 0x15dcb67], rsi                         ; 1400d3642  -> 0x1416b01b0
    mov qword ptr [rip + 0x15dcb68], rdi                         ; 1400d3649  -> 0x1416b01b8
    mov byte ptr [rip + 0x15dcb49], sil                          ; 1400d3650  -> 0x1416b01a0
    lea r9, [rip + 0x107a4a2]                                    ; 1400d3657  -> 0x14114db00 'SelectorPortrait_0/Glow'
    lea edx, [rsi + 0x17]                                        ; 1400d365e
    lea rcx, [rip + 0x15dcb38]                                   ; 1400d3661  -> 0x1416b01a0
    call 0x140534f30                                             ; 1400d3668  -> 0x140534f30 std::string assign
    nop                                                          ; 1400d366d
    mov qword ptr [rip + 0x15dcb4b], rsi                         ; 1400d366e  -> 0x1416b01c0
    mov qword ptr [rip + 0x15dcb54], rsi                         ; 1400d3675  -> 0x1416b01d0
    mov qword ptr [rip + 0x15dcb55], rdi                         ; 1400d367c  -> 0x1416b01d8
    mov byte ptr [rip + 0x15dcb36], sil                          ; 1400d3683  -> 0x1416b01c0
    lea r9, [rip + 0x107a4bf]                                    ; 1400d368a  -> 0x14114db50 'SelectorPortrait_1'
    lea edx, [rsi + 0x12]                                        ; 1400d3691
    lea rcx, [rip + 0x15dcb25]                                   ; 1400d3694  -> 0x1416b01c0
    call 0x140534f30                                             ; 1400d369b  -> 0x140534f30 std::string assign
    nop                                                          ; 1400d36a0
    lea rdx, [rip + 0x107a490]                                   ; 1400d36a1  -> 0x14114db38 'SelectorPortrait_1/Lit'
    lea rcx, [rip + 0x15dcb31]                                   ; 1400d36a8  -> 0x1416b01e0
    call 0x14053478c                                             ; 1400d36af
    nop                                                          ; 1400d36b4
    lea rdx, [rip + 0x107a4cc]                                   ; 1400d36b5  -> 0x14114db88 'SelectorPortrait_1/Used'
    lea rcx, [rip + 0x15dcb3d]                                   ; 1400d36bc  -> 0x1416b0200
    call 0x14053478c                                             ; 1400d36c3
    nop                                                          ; 1400d36c8
    lea rdx, [rip + 0x107a498]                                   ; 1400d36c9  -> 0x14114db68 'SelectorPortrait_1/Locked'
    lea rcx, [rip + 0x15dcb49]                                   ; 1400d36d0  -> 0x1416b0220
    call 0x14053478c                                             ; 1400d36d7
    nop                                                          ; 1400d36dc
    lea rdx, [rip + 0x107a31c]                                   ; 1400d36dd  -> 0x14114da00 'SelectorPortrait_1/Image'
    lea rcx, [rip + 0x15dcb55]                                   ; 1400d36e4  -> 0x1416b0240
    call 0x14053478c                                             ; 1400d36eb
    nop                                                          ; 1400d36f0
    lea rdx, [rip + 0x107a2e8]                                   ; 1400d36f1  -> 0x14114d9e0 'SelectorPortrait_1/HeroColor'
    lea rcx, [rip + 0x15dcb61]                                   ; 1400d36f8  -> 0x1416b0260
    call 0x14053478c                                             ; 1400d36ff
    nop                                                          ; 1400d3704
    lea rdx, [rip + 0x107a32c]                                   ; 1400d3705  -> 0x14114da38 'SelectorPortrait_1/Glow'
    lea rcx, [rip + 0x15dcb6d]                                   ; 1400d370c  -> 0x1416b0280
    call 0x14053478c                                             ; 1400d3713
    nop                                                          ; 1400d3718
    lea rdx, [rip + 0x107a300]                                   ; 1400d3719  -> 0x14114da20 'SelectorPortrait_2'
    lea rcx, [rip + 0x15dcb79]                                   ; 1400d3720  -> 0x1416b02a0
    call 0x14053478c                                             ; 1400d3727
    nop                                                          ; 1400d372c
    lea rdx, [rip + 0x107a334]                                   ; 1400d372d  -> 0x14114da68 'SelectorPortrait_2/Lit'
    lea rcx, [rip + 0x15dcb85]                                   ; 1400d3734  -> 0x1416b02c0
    call 0x14053478c                                             ; 1400d373b
    nop                                                          ; 1400d3740
    lea rdx, [rip + 0x107a308]                                   ; 1400d3741  -> 0x14114da50 'SelectorPortrait_2/Used'
    lea rcx, [rip + 0x15dcb91]                                   ; 1400d3748  -> 0x1416b02e0
    call 0x14053478c                                             ; 1400d374f
    nop                                                          ; 1400d3754
    lea rdx, [rip + 0x107a344]                                   ; 1400d3755  -> 0x14114daa0 'SelectorPortrait_2/Locked'
    lea rcx, [rip + 0x15dcb9d]                                   ; 1400d375c  -> 0x1416b0300
    call 0x14053478c                                             ; 1400d3763
    nop                                                          ; 1400d3768
    lea rdx, [rip + 0x107a310]                                   ; 1400d3769  -> 0x14114da80 'SelectorPortrait_2/Image'
    lea rcx, [rip + 0x15dcba9]                                   ; 1400d3770  -> 0x1416b0320
    call 0x14053478c                                             ; 1400d3777
    nop                                                          ; 1400d377c
    lea rdx, [rip + 0x107a194]                                   ; 1400d377d  -> 0x14114d918 'SelectorPortrait_2/HeroColor'
    lea rcx, [rip + 0x15dcbb5]                                   ; 1400d3784  -> 0x1416b0340
    call 0x14053478c                                             ; 1400d378b
    nop                                                          ; 1400d3790
    lea rdx, [rip + 0x107a168]                                   ; 1400d3791  -> 0x14114d900 'SelectorPortrait_2/Glow'
    lea rcx, [rip + 0x15dcbc1]                                   ; 1400d3798  -> 0x1416b0360
    call 0x14053478c                                             ; 1400d379f
    nop                                                          ; 1400d37a4
    lea rdx, [rip + 0x107a1a4]                                   ; 1400d37a5  -> 0x14114d950 'SelectorPortrait_3'
    lea rcx, [rip + 0x15dcbcd]                                   ; 1400d37ac  -> 0x1416b0380
    call 0x14053478c                                             ; 1400d37b3
    nop                                                          ; 1400d37b8
    lea rdx, [rip + 0x107a178]                                   ; 1400d37b9  -> 0x14114d938 'SelectorPortrait_3/Lit'
    lea rcx, [rip + 0x15dcbd9]                                   ; 1400d37c0  -> 0x1416b03a0
    call 0x14053478c                                             ; 1400d37c7
    nop                                                          ; 1400d37cc
    lea rdx, [rip + 0x107a1b4]                                   ; 1400d37cd  -> 0x14114d988 'SelectorPortrait_3/Used'
    lea rcx, [rip + 0x15dcbe5]                                   ; 1400d37d4  -> 0x1416b03c0
    call 0x14053478c                                             ; 1400d37db
    nop                                                          ; 1400d37e0
    lea rdx, [rip + 0x107a180]                                   ; 1400d37e1  -> 0x14114d968 'SelectorPortrait_3/Locked'
    lea rcx, [rip + 0x15dcbf1]                                   ; 1400d37e8  -> 0x1416b03e0
    call 0x14053478c                                             ; 1400d37ef
    nop                                                          ; 1400d37f4
    lea rdx, [rip + 0x107a1c4]                                   ; 1400d37f5  -> 0x14114d9c0 'SelectorPortrait_3/Image'
    lea rcx, [rip + 0x15dcbfd]                                   ; 1400d37fc  -> 0x1416b0400
    call 0x14053478c                                             ; 1400d3803
    nop                                                          ; 1400d3808
    lea rdx, [rip + 0x107a190]                                   ; 1400d3809  -> 0x14114d9a0 'SelectorPortrait_3/HeroColor'
    lea rcx, [rip + 0x15dcc09]                                   ; 1400d3810  -> 0x1416b0420
    call 0x14053478c                                             ; 1400d3817
    nop                                                          ; 1400d381c
    lea rdx, [rip + 0x107a6dc]                                   ; 1400d381d  -> 0x14114df00 'SelectorPortrait_3/Glow'
    lea rcx, [rip + 0x15dcc15]                                   ; 1400d3824  -> 0x1416b0440
    call 0x14053478c                                             ; 1400d382b
    nop                                                          ; 1400d3830
    lea rdx, [rip + 0x107a6b0]                                   ; 1400d3831  -> 0x14114dee8 'SelectorPortrait_4'
    lea rcx, [rip + 0x15dcc21]                                   ; 1400d3838  -> 0x1416b0460
    call 0x14053478c                                             ; 1400d383f
    nop                                                          ; 1400d3844
    lea rdx, [rip + 0x107a6e4]                                   ; 1400d3845  -> 0x14114df30 'SelectorPortrait_4/Lit'
    lea rcx, [rip + 0x15dcc2d]                                   ; 1400d384c  -> 0x1416b0480
    call 0x14053478c                                             ; 1400d3853
    nop                                                          ; 1400d3858
    lea rdx, [rip + 0x107a6b8]                                   ; 1400d3859  -> 0x14114df18 'SelectorPortrait_4/Used'
    lea rcx, [rip + 0x15dcc39]                                   ; 1400d3860  -> 0x1416b04a0
    call 0x14053478c                                             ; 1400d3867
    nop                                                          ; 1400d386c
    lea rdx, [rip + 0x107a6f4]                                   ; 1400d386d  -> 0x14114df68 'SelectorPortrait_4/Locked'
    lea rcx, [rip + 0x15dcc45]                                   ; 1400d3874  -> 0x1416b04c0
    call 0x14053478c                                             ; 1400d387b
    nop                                                          ; 1400d3880
    lea rdx, [rip + 0x107a6c0]                                   ; 1400d3881  -> 0x14114df48 'SelectorPortrait_4/Image'
    lea rcx, [rip + 0x15dcc51]                                   ; 1400d3888  -> 0x1416b04e0
    call 0x14053478c                                             ; 1400d388f
    nop                                                          ; 1400d3894
    lea rdx, [rip + 0x107a704]                                   ; 1400d3895  -> 0x14114dfa0 'SelectorPortrait_4/HeroColor'
    lea rcx, [rip + 0x15dcc5d]                                   ; 1400d389c  -> 0x1416b0500
    call 0x14053478c                                             ; 1400d38a3
    nop                                                          ; 1400d38a8
    lea rdx, [rip + 0x107a6d8]                                   ; 1400d38a9  -> 0x14114df88 'SelectorPortrait_4/Glow'
    lea rcx, [rip + 0x15dcc69]                                   ; 1400d38b0  -> 0x1416b0520
    call 0x14053478c                                             ; 1400d38b7
    nop                                                          ; 1400d38bc
    lea rdx, [rip + 0x107a564]                                   ; 1400d38bd  -> 0x14114de28 'SelectorPortrait_5'
    lea rcx, [rip + 0x15dcc75]                                   ; 1400d38c4  -> 0x1416b0540
    call 0x14053478c                                             ; 1400d38cb
    nop                                                          ; 1400d38d0
    lea rdx, [rip + 0x107a538]                                   ; 1400d38d1  -> 0x14114de10 'SelectorPortrait_5/Lit'
    lea rcx, [rip + 0x15dcc81]                                   ; 1400d38d8  -> 0x1416b0560
    call 0x14053478c                                             ; 1400d38df
    nop                                                          ; 1400d38e4
    lea rdx, [rip + 0x107a574]                                   ; 1400d38e5  -> 0x14114de60 'SelectorPortrait_5/Used'
    lea rcx, [rip + 0x15dcc8d]                                   ; 1400d38ec  -> 0x1416b0580
    call 0x14053478c                                             ; 1400d38f3
    nop                                                          ; 1400d38f8
    lea rdx, [rip + 0x107a540]                                   ; 1400d38f9  -> 0x14114de40 'SelectorPortrait_5/Locked'
    lea rcx, [rip + 0x15dcc99]                                   ; 1400d3900  -> 0x1416b05a0
    call 0x14053478c                                             ; 1400d3907
    nop                                                          ; 1400d390c
    lea rdx, [rip + 0x107a584]                                   ; 1400d390d  -> 0x14114de98 'SelectorPortrait_5/Image'
    lea rcx, [rip + 0x15dcca5]                                   ; 1400d3914  -> 0x1416b05c0
    call 0x14053478c                                             ; 1400d391b
    nop                                                          ; 1400d3920
    lea rdx, [rip + 0x107a550]                                   ; 1400d3921  -> 0x14114de78 'SelectorPortrait_5/HeroColor'
    lea rcx, [rip + 0x15dccb1]                                   ; 1400d3928  -> 0x1416b05e0
    call 0x14053478c                                             ; 1400d392f
    nop                                                          ; 1400d3934
    lea rdx, [rip + 0x107a594]                                   ; 1400d3935  -> 0x14114ded0 'SelectorPortrait_5/Glow'
    lea rcx, [rip + 0x15dccbd]                                   ; 1400d393c  -> 0x1416b0600
    call 0x14053478c                                             ; 1400d3943
    nop                                                          ; 1400d3948
    lea rdx, [rip + 0x107a568]                                   ; 1400d3949  -> 0x14114deb8 'SelectorPortrait_6'
    lea rcx, [rip + 0x15dccc9]                                   ; 1400d3950  -> 0x1416b0620
    call 0x14053478c                                             ; 1400d3957
    nop                                                          ; 1400d395c
    lea rdx, [rip + 0x107a3ec]                                   ; 1400d395d  -> 0x14114dd50 'SelectorPortrait_6/Lit'
    lea rcx, [rip + 0x15dccd5]                                   ; 1400d3964  -> 0x1416b0640
    call 0x14053478c                                             ; 1400d396b
    nop                                                          ; 1400d3970
    lea rdx, [rip + 0x107a3c0]                                   ; 1400d3971  -> 0x14114dd38 'SelectorPortrait_6/Used'
    lea rcx, [rip + 0x15dcce1]                                   ; 1400d3978  -> 0x1416b0660
    call 0x14053478c                                             ; 1400d397f
    nop                                                          ; 1400d3984
    lea rdx, [rip + 0x107a3fc]                                   ; 1400d3985  -> 0x14114dd88 'SelectorPortrait_6/Locked'
    lea rcx, [rip + 0x15dcced]                                   ; 1400d398c  -> 0x1416b0680
    call 0x14053478c                                             ; 1400d3993
    nop                                                          ; 1400d3998
    lea rdx, [rip + 0x107a3c8]                                   ; 1400d3999  -> 0x14114dd68 'SelectorPortrait_6/Image'
    lea rcx, [rip + 0x15dccf9]                                   ; 1400d39a0  -> 0x1416b06a0
    call 0x14053478c                                             ; 1400d39a7
    nop                                                          ; 1400d39ac
    lea rdx, [rip + 0x107a40c]                                   ; 1400d39ad  -> 0x14114ddc0 'SelectorPortrait_6/HeroColor'
    lea rcx, [rip + 0x15dcd05]                                   ; 1400d39b4  -> 0x1416b06c0
    call 0x14053478c                                             ; 1400d39bb
    nop                                                          ; 1400d39c0
    lea rdx, [rip + 0x107a3e0]                                   ; 1400d39c1  -> 0x14114dda8 'SelectorPortrait_6/Glow'
    lea rcx, [rip + 0x15dcd11]                                   ; 1400d39c8  -> 0x1416b06e0
    call 0x14053478c                                             ; 1400d39cf
    nop                                                          ; 1400d39d4
    lea rdx, [rip + 0x107a41c]                                   ; 1400d39d5  -> 0x14114ddf8 'SelectorPortrait_7'
    lea rcx, [rip + 0x15dcd1d]                                   ; 1400d39dc  -> 0x1416b0700
    call 0x14053478c                                             ; 1400d39e3
    nop                                                          ; 1400d39e8
    lea rdx, [rip + 0x107a3f0]                                   ; 1400d39e9  -> 0x14114dde0 'SelectorPortrait_7/Lit'
    lea rcx, [rip + 0x15dcd29]                                   ; 1400d39f0  -> 0x1416b0720
    call 0x14053478c                                             ; 1400d39f7
    nop                                                          ; 1400d39fc
    lea rdx, [rip + 0x107a284]                                   ; 1400d39fd  -> 0x14114dc88 'SelectorPortrait_7/Used'
    lea rcx, [rip + 0x15dcd35]                                   ; 1400d3a04  -> 0x1416b0740
    call 0x14053478c                                             ; 1400d3a0b
    nop                                                          ; 1400d3a10
    lea rdx, [rip + 0x107a250]                                   ; 1400d3a11  -> 0x14114dc68 'SelectorPortrait_7/Locked'
    lea rcx, [rip + 0x15dcd41]                                   ; 1400d3a18  -> 0x1416b0760
    call 0x14053478c                                             ; 1400d3a1f
    nop                                                          ; 1400d3a24
    lea rdx, [rip + 0x107a294]                                   ; 1400d3a25  -> 0x14114dcc0 'SelectorPortrait_7/Image'
    lea rcx, [rip + 0x15dcd4d]                                   ; 1400d3a2c  -> 0x1416b0780
    call 0x14053478c                                             ; 1400d3a33
    nop                                                          ; 1400d3a38
    lea rdx, [rip + 0x107a260]                                   ; 1400d3a39  -> 0x14114dca0 'SelectorPortrait_7/HeroColor'
    lea rcx, [rip + 0x15dcd59]                                   ; 1400d3a40  -> 0x1416b07a0
    call 0x14053478c                                             ; 1400d3a47
    nop                                                          ; 1400d3a4c
    lea rdx, [rip + 0x107a29c]                                   ; 1400d3a4d  -> 0x14114dcf0 'SelectorPortrait_7/Glow'
    lea rcx, [rip + 0x15dcd65]                                   ; 1400d3a54  -> 0x1416b07c0
    call 0x14053478c                                             ; 1400d3a5b
    nop                                                          ; 1400d3a60
    lea rcx, [rip + 0xdcd498]                                    ; 1400d3a61  -> 0x140ea0f00
    mov rsi, qword ptr [rsp + 0x30]                              ; 1400d3a68
    add rsp, 0x20                                                ; 1400d3a6d
    pop rdi                                                      ; 1400d3a71
    jmp 0x14186e920                                              ; 1400d3a72

org 0x14054e720
    mov edx, 0x100                                               ; 14054e720

org 0x14064fa4a
    mov word ptr [rbx + 0xf8], ax                                ; 14064fa4a
    mov qword ptr [rbx + 0x100], rbp                             ; 14064fa51
    mov qword ptr [rbx + 0x108], rbp                             ; 14064fa58
    mov qword ptr [rbx + 0x110], rbp                             ; 14064fa5f
    mov qword ptr [rbx + 0x118], rbp                             ; 14064fa66
    mov dword ptr [rbx + 0x120], ebp                             ; 14064fa6d

org 0x14064fcf2
    cmp dword ptr [rbx + 0x120], 0                               ; 14064fcf2
    je 0x14064fd03                                               ; 14064fcf9
    add dword ptr [rbx + 0x120], eax                             ; 14064fcfb

org 0x14064fe17
    jmp 0x140f6aca0                                              ; 14064fe17
    nop                                                          ; 14064fe1c
    nop                                                          ; 14064fe1d
    nop                                                          ; 14064fe1e
    nop                                                          ; 14064fe1f
    xorps xmm1, xmm1                                             ; 14064fe20
    .bytes 33c0                                                 ; 14064fe23  xor eax, eax  (exact original encoding)
    mov qword ptr [rbp - 0x20], rax                              ; 14064fe25
    lea edi, [rax + 9]                                           ; 14064fe29
    jmp 0x14064fe48                                              ; 14064fe2c
    mov eax, dword ptr [rbx + 0x18]                              ; 14064fe2e
    lea rcx, [rax + rax*2]                                       ; 14064fe31
    movups xmmword ptr [rbx + rcx*8 + 0x20], xmm1                ; 14064fe35
    movsd xmm0, qword ptr [rbp - 0x20]                           ; 14064fe3a
    movsd qword ptr [rbx + rcx*8 + 0x30], xmm0                   ; 14064fe3f
    inc dword ptr [rbx + 0x18]                                   ; 14064fe45
    cmp dword ptr [rbx + 0x18], edi                              ; 14064fe48
    jb 0x14064fe2e                                               ; 14064fe4b
    lea rcx, [rbp + 0x30]                                        ; 14064fe4d
    call 0x1405b2ff4                                             ; 14064fe51
    movzx eax, word ptr [rax]                                    ; 14064fe56
    mov word ptr [rbx + 0xf8], ax                                ; 14064fe59

org 0x14064feeb
    test byte ptr [rax + rbx + 0xf8], dl                         ; 14064feeb

org 0x14064ff48
    test byte ptr [rax + rbx + 0xf8], dl                         ; 14064ff48

org 0x14064ffb7
    test byte ptr [rax + rbx + 0xf8], dl                         ; 14064ffb7

org 0x14065000b
    test byte ptr [rax + rbx + 0xf8], dl                         ; 14065000b
    jne 0x140650018                                              ; 140650012
    .bytes 32c0                                                 ; 140650014  xor al, al  (exact original encoding)
    jmp 0x14065001a                                              ; 140650016
    mov al, 1                                                    ; 140650018
    mov byte ptr [rdi + 1], al                                   ; 14065001a
    inc esi                                                      ; 14065001d
    add r13, 4                                                   ; 14065001f
    add rdi, 0x18                                                ; 140650023
    add r14, 4                                                   ; 140650027
    cmp esi, 9                                                   ; 14065002b

org 0x140650b0d
    test byte ptr [rax + r11 + 0xf8], r8b                        ; 140650b0d

org 0x140650b63
    test byte ptr [rax + r11 + 0xf8], dl                         ; 140650b63

org 0x140650c68
    cmp word ptr [rbx + 0xf8], ax                                ; 140650c68
    je 0x140650d65                                               ; 140650c6f
    mov word ptr [rbx + 0xf8], ax                                ; 140650c75

org 0x140650cf6
    test byte ptr [rax + rbx + 0xf8], dl                         ; 140650cf6
    jne 0x140650d03                                              ; 140650cfd
    .bytes 32c0                                                 ; 140650cff  xor al, al  (exact original encoding)
    jmp 0x140650d05                                              ; 140650d01
    mov al, 1                                                    ; 140650d03
    mov byte ptr [r8 - 2], al                                    ; 140650d05
    mov r9d, dword ptr [r10 + 0xe4]                              ; 140650d09
    test r9d, r9d                                                ; 140650d10
    je 0x140650d36                                               ; 140650d13
    .bytes 418bc1                                               ; 140650d15  mov eax, r9d  (exact original encoding)
    .bytes 418bc9                                               ; 140650d18  mov ecx, r9d  (exact original encoding)
    and ecx, 7                                                   ; 140650d1b
    shr rax, 3                                                   ; 140650d1e
    mov edx, 1                                                   ; 140650d22
    shl edx, cl                                                  ; 140650d27
    test byte ptr [rax + rbx + 0xf8], dl                         ; 140650d29

org 0x140650e98
    mov rcx, qword ptr [rdi + rax*8 + 0x100]                     ; 140650e98
    mov eax, dword ptr [rcx + 0x78]                              ; 140650ea0
    mov dword ptr [rdi + 0x130], eax                             ; 140650ea3
    lea rcx, [rax + rax*2]                                       ; 140650ea9
    mov byte ptr [rdi + rcx*8 + 0x2c], bl                        ; 140650ead
    movsxd rax, dword ptr [rdi + 0x134]                          ; 140650eb1
    mov qword ptr [rdi + rax*8 + 0x100], rbx                     ; 140650eb8

org 0x14065114c
    mov qword ptr [rcx + rdx*8 + 0x100], rax                     ; 14065114c
    movsxd rcx, dword ptr [rcx + 0x134]                          ; 140651154
    mov r13, qword ptr [rbx + rcx*8 + 0x100]                     ; 14065115b

org 0x14065126a
    mov qword ptr [rbx + rcx*8 + 0x100], rax                     ; 14065126a
    movsxd r8, dword ptr [rbx + 0x134]                           ; 140651272
    mov rcx, qword ptr [rbx + r8*8 + 0x100]                      ; 140651279

org 0x1406512ca
    mov rcx, qword ptr [rbx + r8*8 + 0x100]                      ; 1406512ca
    mov r9d, dword ptr [rcx + 0x28]                              ; 1406512d2
    lea rcx, [rip + 0xafc11b]                                    ; 1406512d6  -> 0x14114d3f8 'clientEvent_change_portrait'
    .bytes 8bd6                                                 ; 1406512dd  mov edx, esi  (exact original encoding)
    .bytes 418ac7                                               ; 1406512df  mov al, r15b  (exact original encoding)
    .bytes 4803cf                                               ; 1406512e2  add rcx, rdi  (exact original encoding)
    movsx eax, al                                                ; 1406512e5
    .bytes 33c2                                                 ; 1406512e8  xor eax, edx  (exact original encoding)
    imul edx, eax, 0x1000193                                     ; 1406512ea
    mov al, byte ptr [rcx]                                       ; 1406512f0
    test al, al                                                  ; 1406512f2
    jne 0x1406512e2                                              ; 1406512f4
    call 0x140652ff0                                             ; 1406512f6
    movsxd rax, dword ptr [rbx + 0x134]                          ; 1406512fb
    mov r8, qword ptr [rbx + rax*8 + 0x100]                      ; 140651302

org 0x140651399
    mov qword ptr [rbx + rax*8 + 0x100], rdx                     ; 140651399
    movsxd r8, dword ptr [rbx + 0x134]                           ; 1406513a1
    mov r13, qword ptr [rbx + r8*8 + 0x100]                      ; 1406513a8

org 0x140651557
    test byte ptr [rax + rbx + 0xf8], dl                         ; 140651557

org 0x1406515a5
    test byte ptr [rax + rbx + 0xf8], dl                         ; 1406515a5
    .bytes 418ac5                                               ; 1406515ac  mov al, r13b  (exact original encoding)
    je 0x1406515b4                                               ; 1406515af
    .bytes 408ac7                                               ; 1406515b1  mov al, dil  (exact original encoding)
    mov byte ptr [rsi + 2], al                                   ; 1406515b4
    .bytes 4403f7                                               ; 1406515b7  add r14d, edi  (exact original encoding)
    add rsi, 0x18                                                ; 1406515ba
    cmp r14d, 9                                                  ; 1406515be

org 0x14065199a
    mov rdx, qword ptr [rbp + rax*8 + 0x100]                     ; 14065199a

org 0x140651aea
    mov ecx, 9                                                   ; 140651aea

org 0x140651b7d
    cmp ecx, 9                                                   ; 140651b7d

org 0x140651f94
    mov rdx, qword ptr [rdi + 0x100]                             ; 140651f94

org 0x1406520e7
    lea rbx, [rdi + 0x100]                                       ; 1406520e7

org 0x14065268c
    mov qword ptr [rsi + rcx*8 + 0x100], rax                     ; 14065268c
    mov qword ptr [rsi + 0x150], r14                             ; 140652694
    call 0x1407ca0c0                                             ; 14065269b
    cmp dword ptr [rsi + 0x144], 1                               ; 1406526a0
    setne dl                                                     ; 1406526a7
    .bytes 488bce                                               ; 1406526aa  mov rcx, rsi  (exact original encoding)
    call 0x140651ba0                                             ; 1406526ad
    mov qword ptr [rbp - 0x10], r14                              ; 1406526b2
    mov qword ptr [rbp - 8], r14                                 ; 1406526b6
    mov qword ptr [rbp - 0x20], r14                              ; 1406526ba
    mov qword ptr [rbp - 0x18], r14                              ; 1406526be
    movsxd rax, dword ptr [rsi + 0x134]                          ; 1406526c2
    mov rdx, qword ptr [rsi + rax*8 + 0x100]                     ; 1406526c9
    sub rdx, -0x80                                               ; 1406526d1
    lea rcx, [rbp - 0x10]                                        ; 1406526d5
    call 0x14054c764                                             ; 1406526d9
    movsxd rax, dword ptr [rsi + 0x134]                          ; 1406526de
    mov rdx, qword ptr [rsi + rax*8 + 0x100]                     ; 1406526e5

org 0x140652993
    mov rax, qword ptr [rbx + rdx*8 + 0x100]                     ; 140652993
    cmp qword ptr [r8], rax                                      ; 14065299b
    jne 0x1406529b4                                              ; 14065299e
    and qword ptr [rbx + rdx*8 + 0x100], 0                       ; 1406529a0
    .bytes 418af2                                               ; 1406529a9  mov sil, r10b  (exact original encoding)
    .bytes 4103fa                                               ; 1406529ac  add edi, r10d  (exact original encoding)
    mov rcx, qword ptr [rsp + 0x30]                              ; 1406529af
    .bytes 418ad2                                               ; 1406529b4  mov dl, r10b  (exact original encoding)
    jmp 0x1406529c8                                              ; 1406529b7
    .bytes 32d2                                                 ; 1406529b9  xor dl, dl  (exact original encoding)
    .bytes 498bc0                                               ; 1406529bb  mov rax, r8  (exact original encoding)
    test r14, r14                                                ; 1406529be
    cmovne rax, r14                                              ; 1406529c1
    .bytes 4c8bf0                                               ; 1406529c5  mov r14, rax  (exact original encoding)
    mov byte ptr [r8 + 0x10], dl                                 ; 1406529c8
    .bytes 4503ca                                               ; 1406529cc  add r9d, r10d  (exact original encoding)
    add r8, 0x18                                                 ; 1406529cf
    cmp r9d, 9                                                   ; 1406529d3

org 0x140652ced
    mov rdx, qword ptr [rbx + rax*8 + 0x100]                     ; 140652ced
    sub rdx, -0x80                                               ; 140652cf5
    lea rcx, [rbp - 0x10]                                        ; 140652cf9
    call 0x14054c764                                             ; 140652cfd
    movsxd rax, dword ptr [rbx + 0x134]                          ; 140652d02
    mov rdx, qword ptr [rbx + rax*8 + 0x100]                     ; 140652d09

org 0x140653bf9
    lea rbx, [rip + 0x105c4e0]                                   ; 140653bf9  -> 0x1416b00e0

org 0x140653cd3
    lea rbx, [rip + 0x105c406]                                   ; 140653cd3  -> 0x1416b00e0

org 0x140653d53
    cmp r14d, 9                                                  ; 140653d53

org 0x1406547cf
    lea r13, [rip + 0x105b90a]                                   ; 1406547cf  -> 0x1416b00e0

org 0x140654920
    cmp ebp, 9                                                   ; 140654920

org 0x140655455
    lea r15, [rip + 0x105ac84]                                   ; 140655455  -> 0x1416b00e0

org 0x140655784
    lea rdx, [rip + 0x105a955]                                   ; 140655784  -> 0x1416b00e0
    sub rdx, -0x80                                               ; 14065578b
    .bytes 4903d6                                               ; 14065578f  add rdx, r14  (exact original encoding)
    lea r9, [rip + 0x1054967]                                    ; 140655792  -> 0x1416aa100
    .bytes 488bcb                                               ; 140655799  mov rcx, rbx  (exact original encoding)
    call 0x1407e4c40                                             ; 14065579c
    mov rcx, qword ptr [rdi]                                     ; 1406557a1
    mov rdx, qword ptr [rbx + 0x140]                             ; 1406557a4
    lea r8, [rcx + 0x190]                                        ; 1406557ab
    test rdx, rdx                                                ; 1406557b2
    je 0x1406557d7                                               ; 1406557b5
    lea rdx, [rip + 0x105a922]                                   ; 1406557b7  -> 0x1416b00e0

org 0x1406558c9
    lea rax, [rip + 0x105a830]                                   ; 1406558c9  -> 0x1416b0100

org 0x140655915
    cmp r15d, 9                                                  ; 140655915

org 0x140655bb1
    jmp 0x14186ef70                                              ; 140655bb1
    nop                                                          ; 140655bb6
    nop                                                          ; 140655bb7
    nop                                                          ; 140655bb8
    nop                                                          ; 140655bb9

org 0x140683667
    jmp 0x14186f000                                              ; 140683667
    nop                                                          ; 14068366c
    nop                                                          ; 14068366d
    nop                                                          ; 14068366e
    nop                                                          ; 14068366f

org 0x140683b00
    lea rdx, [rip + 0x11eac51]                                   ; 140683b00  -> 0x14186e758 'abilitybutton_rebirth_shredder_none'

org 0x140683ba4
    lea rdx, [rip + 0x11eabad]                                   ; 140683ba4  -> 0x14186e758 'abilitybutton_rebirth_shredder_none'

org 0x140683fd6
    lea rdx, [rip + 0x11ea77b]                                   ; 140683fd6  -> 0x14186e758 'abilitybutton_rebirth_shredder_none'

org 0x1406a66b7
    cmp dword ptr [rcx + 0xb8], 0                                ; 1406a66b7
    .bytes 488bd9                                               ; 1406a66be  mov rbx, rcx  (exact original encoding)
    je 0x1406a66cc                                               ; 1406a66c1
    add dword ptr [rcx + 0xb8], -1                               ; 1406a66c3

org 0x1406a6761
    mov ebx, 0x100                                               ; 1406a6761

org 0x1406a67db
    mov dword ptr [rsi + 0xb8], r15d                             ; 1406a67db
    jmp 0x1406a67e7                                              ; 1406a67e2
    .bytes 498bf7                                               ; 1406a67e4  mov rsi, r15  (exact original encoding)
    mov qword ptr [rip + 0xf50092], rsi                          ; 1406a67e7  -> 0x1415f6880
    xorps xmm0, xmm0                                             ; 1406a67ee
    movups xmmword ptr [rbp - 0x39], xmm0                        ; 1406a67f1
    mov qword ptr [rbp - 0x39], r15                              ; 1406a67f5
    mov qword ptr [rbp - 0x31], r15                              ; 1406a67f9
    mov r12d, 9                                                  ; 1406a67fd
    cmp dword ptr [rsi + 0x20], r12d                             ; 1406a6803
    jae 0x1406a6829                                              ; 1406a6807
    lea rbx, [rsi + 0x28]                                        ; 1406a6809
    mov ecx, dword ptr [rsi + 0x20]                              ; 1406a680d
    shl rcx, 4                                                   ; 1406a6810
    .bytes 4803cb                                               ; 1406a6814  add rcx, rbx  (exact original encoding)
    lea rdx, [rbp - 0x39]                                        ; 1406a6817
    call 0x140655d40                                             ; 1406a681b
    inc dword ptr [rsi + 0x20]                                   ; 1406a6820
    cmp dword ptr [rsi + 0x20], r12d                             ; 1406a6823
    jb 0x1406a680d                                               ; 1406a6827
    jmp 0x1406a683f                                              ; 1406a6829
    mov eax, dword ptr [rsi + 0xb8]                              ; 1406a682b
    mov dword ptr [rsi + rax*4 + 0xbc], r15d                     ; 1406a6831
    inc dword ptr [rsi + 0xb8]                                   ; 1406a6839
    cmp dword ptr [rsi + 0xb8], r12d                             ; 1406a683f

org 0x1406a6c51
    mov dword ptr [rsi + rcx*4 + 0xbc], eax                      ; 1406a6c51

org 0x1406ad1a0
    jmp 0x14186f170                                              ; 1406ad1a0
    nop                                                          ; 1406ad1a5
    nop                                                          ; 1406ad1a6

org 0x14072e3e4
    jmp 0x14186ef50                                              ; 14072e3e4
    nop                                                          ; 14072e3e9
    nop                                                          ; 14072e3ea
    nop                                                          ; 14072e3eb

org 0x14074278c
    jmp 0x14186efc0                                              ; 14074278c
    nop                                                          ; 140742791
    nop                                                          ; 140742792
    nop                                                          ; 140742793

org 0x140883e52
    jmp 0x14186eb50                                              ; 140883e52
    nop                                                          ; 140883e57
    nop                                                          ; 140883e58

org 0x140883ead
    jmp 0x14186eb70                                              ; 140883ead
    nop                                                          ; 140883eb2
    nop                                                          ; 140883eb3

org 0x140883efe
    jmp 0x14186eb90                                              ; 140883efe
    nop                                                          ; 140883f03
    nop                                                          ; 140883f04

org 0x140883f4f
    jmp 0x14186ebb0                                              ; 140883f4f
    nop                                                          ; 140883f54
    nop                                                          ; 140883f55

org 0x140883fa0
    jmp 0x14186ebd0                                              ; 140883fa0
    nop                                                          ; 140883fa5
    nop                                                          ; 140883fa6

org 0x140884878
    jmp 0x14186ebf0                                              ; 140884878
    nop                                                          ; 14088487d
    nop                                                          ; 14088487e

org 0x140885769
    jmp 0x14186ec10                                              ; 140885769
    nop                                                          ; 14088576e
    nop                                                          ; 14088576f

org 0x1408864e7
    jmp 0x14186ec30                                              ; 1408864e7
    nop                                                          ; 1408864ec
    nop                                                          ; 1408864ed

org 0x1408872cc
    jmp 0x14186ec70                                              ; 1408872cc
    nop                                                          ; 1408872d1
    nop                                                          ; 1408872d2

org 0x140887990
    jmp 0x14186ec90                                              ; 140887990
    nop                                                          ; 140887995
    nop                                                          ; 140887996

org 0x140887c98
    jmp 0x14186ec50                                              ; 140887c98
    nop                                                          ; 140887c9d
    nop                                                          ; 140887c9e

org 0x140888cc0
    jmp 0x14186ecb0                                              ; 140888cc0
    nop                                                          ; 140888cc5
    nop                                                          ; 140888cc6

org 0x140888e72
    jmp 0x14186ecf0                                              ; 140888e72
    nop                                                          ; 140888e77
    nop                                                          ; 140888e78

org 0x140888f76
    jmp 0x14186ecd0                                              ; 140888f76
    nop                                                          ; 140888f7b
    nop                                                          ; 140888f7c

org 0x140a05c9d
    jmp 0x14186ed10                                              ; 140a05c9d
    nop                                                          ; 140a05ca2
    nop                                                          ; 140a05ca3

org 0x140a06a7c
    jmp 0x14186ed30                                              ; 140a06a7c
    nop                                                          ; 140a06a81
    nop                                                          ; 140a06a82

org 0x140b5bd09
    jmp 0x14186ed50                                              ; 140b5bd09
    nop                                                          ; 140b5bd0e
    nop                                                          ; 140b5bd0f
    nop                                                          ; 140b5bd10
    nop                                                          ; 140b5bd11
    nop                                                          ; 140b5bd12
    nop                                                          ; 140b5bd13

org 0x140b5bd85
    jmp 0x14186edb0                                              ; 140b5bd85
    nop                                                          ; 140b5bd8a
    nop                                                          ; 140b5bd8b
    nop                                                          ; 140b5bd8c

org 0x140b5be1b
    jmp 0x14186edd0                                              ; 140b5be1b
    nop                                                          ; 140b5be20
    nop                                                          ; 140b5be21
    nop                                                          ; 140b5be22

org 0x140b5be95
    jmp 0x14186edf0                                              ; 140b5be95
    nop                                                          ; 140b5be9a
    nop                                                          ; 140b5be9b
    nop                                                          ; 140b5be9c

org 0x140b5bf10
    jmp 0x14186ee10                                              ; 140b5bf10
    nop                                                          ; 140b5bf15
    nop                                                          ; 140b5bf16
    nop                                                          ; 140b5bf17

org 0x140b5bf92
    jmp 0x14186ee30                                              ; 140b5bf92
    nop                                                          ; 140b5bf97
    nop                                                          ; 140b5bf98
    nop                                                          ; 140b5bf99

org 0x140b5c070
    jmp 0x14186ee50                                              ; 140b5c070
    nop                                                          ; 140b5c075
    nop                                                          ; 140b5c076
    nop                                                          ; 140b5c077

org 0x140e2b942
    lea rcx, [rip + 0x884797]                                    ; 140e2b942  -> 0x1416b00e0
    jmp 0x1405347fc                                              ; 140e2b949
    lea rcx, [rip + 0x8847ab]                                    ; 140e2b94e  -> 0x1416b0100
    jmp 0x1405347fc                                              ; 140e2b955
    lea rcx, [rip + 0x8847bf]                                    ; 140e2b95a  -> 0x1416b0120
    jmp 0x1405347fc                                              ; 140e2b961
    lea rcx, [rip + 0x8847d3]                                    ; 140e2b966  -> 0x1416b0140
    jmp 0x1405347fc                                              ; 140e2b96d
    lea rcx, [rip + 0x8847e7]                                    ; 140e2b972  -> 0x1416b0160
    jmp 0x1405347fc                                              ; 140e2b979
    lea rcx, [rip + 0x8847fb]                                    ; 140e2b97e  -> 0x1416b0180
    jmp 0x1405347fc                                              ; 140e2b985
    lea rcx, [rip + 0x88474f]                                    ; 140e2b98a  -> 0x1416b00e0
    jmp 0x140653490                                              ; 140e2b991
    lea rcx, [rip + 0x884823]                                    ; 140e2b996  -> 0x1416b01c0
    jmp 0x1405347fc                                              ; 140e2b99d
    lea rcx, [rip + 0x884837]                                    ; 140e2b9a2  -> 0x1416b01e0
    jmp 0x1405347fc                                              ; 140e2b9a9
    lea rcx, [rip + 0x88484b]                                    ; 140e2b9ae  -> 0x1416b0200
    jmp 0x1405347fc                                              ; 140e2b9b5
    lea rcx, [rip + 0x88485f]                                    ; 140e2b9ba  -> 0x1416b0220
    jmp 0x1405347fc                                              ; 140e2b9c1
    lea rcx, [rip + 0x884873]                                    ; 140e2b9c6  -> 0x1416b0240
    jmp 0x1405347fc                                              ; 140e2b9cd
    lea rcx, [rip + 0x884887]                                    ; 140e2b9d2  -> 0x1416b0260
    jmp 0x1405347fc                                              ; 140e2b9d9
    lea rcx, [rip + 0x8846fb]                                    ; 140e2b9de  -> 0x1416b00e0
    add rcx, 0xe0                                                ; 140e2b9e5
    jmp 0x140653490                                              ; 140e2b9ec
    lea rcx, [rip + 0x8848a8]                                    ; 140e2b9f1  -> 0x1416b02a0
    jmp 0x1405347fc                                              ; 140e2b9f8
    lea rcx, [rip + 0x8848bc]                                    ; 140e2b9fd  -> 0x1416b02c0
    jmp 0x1405347fc                                              ; 140e2ba04
    lea rcx, [rip + 0x8848d0]                                    ; 140e2ba09  -> 0x1416b02e0
    jmp 0x1405347fc                                              ; 140e2ba10
    lea rcx, [rip + 0x8848e4]                                    ; 140e2ba15  -> 0x1416b0300
    jmp 0x1405347fc                                              ; 140e2ba1c
    lea rcx, [rip + 0x8848f8]                                    ; 140e2ba21  -> 0x1416b0320
    jmp 0x1405347fc                                              ; 140e2ba28
    lea rcx, [rip + 0x88490c]                                    ; 140e2ba2d  -> 0x1416b0340
    jmp 0x1405347fc                                              ; 140e2ba34
    lea rcx, [rip + 0x8846a0]                                    ; 140e2ba39  -> 0x1416b00e0
    add rcx, 0x1c0                                               ; 140e2ba40
    jmp 0x140653490                                              ; 140e2ba47
    lea rcx, [rip + 0x88492d]                                    ; 140e2ba4c  -> 0x1416b0380
    jmp 0x1405347fc                                              ; 140e2ba53
    lea rcx, [rip + 0x884941]                                    ; 140e2ba58  -> 0x1416b03a0
    jmp 0x1405347fc                                              ; 140e2ba5f
    lea rcx, [rip + 0x884955]                                    ; 140e2ba64  -> 0x1416b03c0
    jmp 0x1405347fc                                              ; 140e2ba6b
    lea rcx, [rip + 0x884969]                                    ; 140e2ba70  -> 0x1416b03e0
    jmp 0x1405347fc                                              ; 140e2ba77
    lea rcx, [rip + 0x88497d]                                    ; 140e2ba7c  -> 0x1416b0400
    jmp 0x1405347fc                                              ; 140e2ba83
    lea rcx, [rip + 0x884991]                                    ; 140e2ba88  -> 0x1416b0420
    jmp 0x1405347fc                                              ; 140e2ba8f
    lea rcx, [rip + 0x884645]                                    ; 140e2ba94  -> 0x1416b00e0
    add rcx, 0x2a0                                               ; 140e2ba9b
    jmp 0x140653490                                              ; 140e2baa2
    lea rcx, [rip + 0x8849b2]                                    ; 140e2baa7  -> 0x1416b0460
    jmp 0x1405347fc                                              ; 140e2baae
    lea rcx, [rip + 0x8849c6]                                    ; 140e2bab3  -> 0x1416b0480
    jmp 0x1405347fc                                              ; 140e2baba
    lea rcx, [rip + 0x8849da]                                    ; 140e2babf  -> 0x1416b04a0
    jmp 0x1405347fc                                              ; 140e2bac6
    lea rcx, [rip + 0x8849ee]                                    ; 140e2bacb  -> 0x1416b04c0
    jmp 0x1405347fc                                              ; 140e2bad2
    lea rcx, [rip + 0x884a02]                                    ; 140e2bad7  -> 0x1416b04e0
    jmp 0x1405347fc                                              ; 140e2bade
    lea rcx, [rip + 0x884a16]                                    ; 140e2bae3  -> 0x1416b0500
    jmp 0x1405347fc                                              ; 140e2baea
    lea rcx, [rip + 0x8845ea]                                    ; 140e2baef  -> 0x1416b00e0
    add rcx, 0x380                                               ; 140e2baf6
    jmp 0x140653490                                              ; 140e2bafd
    lea rcx, [rip + 0x884a37]                                    ; 140e2bb02  -> 0x1416b0540
    jmp 0x1405347fc                                              ; 140e2bb09
    lea rcx, [rip + 0x884a4b]                                    ; 140e2bb0e  -> 0x1416b0560
    jmp 0x1405347fc                                              ; 140e2bb15
    lea rcx, [rip + 0x884a5f]                                    ; 140e2bb1a  -> 0x1416b0580
    jmp 0x1405347fc                                              ; 140e2bb21
    lea rcx, [rip + 0x884a73]                                    ; 140e2bb26  -> 0x1416b05a0
    jmp 0x1405347fc                                              ; 140e2bb2d
    lea rcx, [rip + 0x884a87]                                    ; 140e2bb32  -> 0x1416b05c0
    jmp 0x1405347fc                                              ; 140e2bb39
    lea rcx, [rip + 0x884a9b]                                    ; 140e2bb3e  -> 0x1416b05e0
    jmp 0x1405347fc                                              ; 140e2bb45
    lea rcx, [rip + 0x88458f]                                    ; 140e2bb4a  -> 0x1416b00e0
    add rcx, 0x460                                               ; 140e2bb51
    jmp 0x140653490                                              ; 140e2bb58
    lea rcx, [rip + 0x884abc]                                    ; 140e2bb5d  -> 0x1416b0620
    jmp 0x1405347fc                                              ; 140e2bb64
    lea rcx, [rip + 0x884ad0]                                    ; 140e2bb69  -> 0x1416b0640
    jmp 0x1405347fc                                              ; 140e2bb70
    lea rcx, [rip + 0x884ae4]                                    ; 140e2bb75  -> 0x1416b0660
    jmp 0x1405347fc                                              ; 140e2bb7c
    lea rcx, [rip + 0x884af8]                                    ; 140e2bb81  -> 0x1416b0680
    jmp 0x1405347fc                                              ; 140e2bb88
    lea rcx, [rip + 0x884b0c]                                    ; 140e2bb8d  -> 0x1416b06a0
    jmp 0x1405347fc                                              ; 140e2bb94
    lea rcx, [rip + 0x884b20]                                    ; 140e2bb99  -> 0x1416b06c0
    jmp 0x1405347fc                                              ; 140e2bba0
    lea rcx, [rip + 0x884534]                                    ; 140e2bba5  -> 0x1416b00e0
    add rcx, 0x540                                               ; 140e2bbac
    jmp 0x140653490                                              ; 140e2bbb3
    lea rcx, [rip + 0x884b41]                                    ; 140e2bbb8  -> 0x1416b0700
    jmp 0x1405347fc                                              ; 140e2bbbf
    lea rcx, [rip + 0x884b55]                                    ; 140e2bbc4  -> 0x1416b0720
    jmp 0x1405347fc                                              ; 140e2bbcb
    lea rcx, [rip + 0x884b69]                                    ; 140e2bbd0  -> 0x1416b0740
    jmp 0x1405347fc                                              ; 140e2bbd7
    lea rcx, [rip + 0x884b7d]                                    ; 140e2bbdc  -> 0x1416b0760
    jmp 0x1405347fc                                              ; 140e2bbe3
    lea rcx, [rip + 0x884b91]                                    ; 140e2bbe8  -> 0x1416b0780
    jmp 0x1405347fc                                              ; 140e2bbef
    lea rcx, [rip + 0x884ba5]                                    ; 140e2bbf4  -> 0x1416b07a0

org 0x140ea0f12
    lea rcx, [rip + 0x80f1c7]                                    ; 140ea0f12  -> 0x1416b00e0

; ---- new code and data (caves)

org 0x140f6ac80
  ; L_140f6ac80
    push rsi                                                     ; 140f6ac80
    push rdi                                                     ; 140f6ac81
    push rcx                                                     ; 140f6ac82
    lea rsi, [rip + 0x76]                                        ; 140f6ac83  -> 0x140f6ad00 'SP8'
    lea rdi, [rip + 0x745b4f]                                    ; 140f6ac8a  -> 0x1416b07e0
    mov ecx, 0xe0                                                ; 140f6ac91
    rep movsb byte ptr [rdi], byte ptr [rsi]                     ; 140f6ac96
    pop rcx                                                      ; 140f6ac98
    pop rdi                                                      ; 140f6ac99
    pop rsi                                                      ; 140f6ac9a
    jmp 0x140e1ab5c                                              ; 140f6ac9b
  ; ENTRY_140f6aca0
    mov al, byte ptr [rbp + 0x30]                                ; 140f6aca0
    mov byte ptr [rbx + 0x16c], al                               ; 140f6aca3
    mov byte ptr [rbx + 0x16d], 1                                ; 140f6aca9
    jmp 0x14064fe20                                              ; 140f6acb0

org 0x140f6ad00
    .bytes 53503800000000000000000000000000                     ; 140f6ad00  SP8.............
    .bytes 03000000000000000f00000000000000                     ; 140f6ad10  ................
    .bytes 5350382f4c6974000000000000000000                     ; 140f6ad20  SP8/Lit.........
    .bytes 07000000000000000f00000000000000                     ; 140f6ad30  ................
    .bytes 5350382f557365640000000000000000                     ; 140f6ad40  SP8/Used........
    .bytes 08000000000000000f00000000000000                     ; 140f6ad50  ................
    .bytes 5350382f4c6f636b6564000000000000                     ; 140f6ad60  SP8/Locked......
    .bytes 0a000000000000000f00000000000000                     ; 140f6ad70  ................
    .bytes 5350382f496d61676500000000000000                     ; 140f6ad80  SP8/Image.......
    .bytes 09000000000000000f00000000000000                     ; 140f6ad90  ................
    .bytes 5350382f4865726f436f6c6f72000000                     ; 140f6ada0  SP8/HeroColor...
    .bytes 0d000000000000000f00000000000000                     ; 140f6adb0  ................
    .bytes 5350382f476c6f770000000000000000                     ; 140f6adc0  SP8/Glow........
    .bytes 08000000000000000f                                   ; 140f6add0  .........

org 0x14186e000
    .bytes 00000000000000000000000000000000                     ; 14186e000  ................
    .bytes 0000203fcdcccc3e0000000000000000                     ; 14186e010  .. ?...>........
    .bytes a4e311550c018b19a0d35746d69c2737                     ; 14186e020  ...U......WF..'7
    .bytes 1afa92d1000000000000000000000000                     ; 14186e030  ................
    .bytes 00000000000000000000000000000000                     ; 14186e040  ................
    .bytes 00000000000000000000000000000000                     ; 14186e050  ................
    .bytes 00000000000000000000000000000000                     ; 14186e060  ................
    .bytes 00000000000000000000000000000000                     ; 14186e070  ................
    .bytes 00000000000000000000000000000000                     ; 14186e080  ................
    .bytes 00000000000000000000000000000000                     ; 14186e090  ................
    .bytes 00000000000000000000000000000000                     ; 14186e0a0  ................
    .bytes 00000000000000000000000000000000                     ; 14186e0b0  ................
    .bytes 00000000000000000000000000000000                     ; 14186e0c0  ................
    .bytes 00000000000000000000000000000000                     ; 14186e0d0  ................
    .bytes 00000000000000000000000000000000                     ; 14186e0e0  ................
    .bytes 00000000000000000000000000000000                     ; 14186e0f0  ................
    .bytes 00000000000000000000000000000000                     ; 14186e100  ................
    .bytes 00000000000000000000000000000000                     ; 14186e110  ................
    .bytes 00000000000000000000000000000000                     ; 14186e120  ................
    .bytes 00000000000000000000000000000000                     ; 14186e130  ................
    .bytes 85000000000000000000000000000000                     ; 14186e140  ................
    .bytes 0d000000000000000000000000000000                     ; 14186e150  ................
    .bytes 44000000000000000000000000000000                     ; 14186e160  D...............
    .bytes 00000000000000000000000000000000                     ; 14186e170  ................
    .bytes 00000000000000000000000000000000                     ; 14186e180  ................
    .bytes 00000000000000000000000000000000                     ; 14186e190  ................
    .bytes 00000000000000000000000000000000                     ; 14186e1a0  ................
    .bytes 4d006100730074006500720020006f00                     ; 14186e1b0  M.a.s.t.e.r. .o.
    .bytes 66002000740068006500200046006f00                     ; 14186e1c0  f. .t.h.e. .F.o.
    .bytes 6f007400200043006c0061006e002e00                     ; 14186e1d0  o.t. .C.l.a.n...
    .bytes 20004f0072006f006b00750020005300                     ; 14186e1e0   .O.r.o.k.u. .S.
    .bytes 61006b00690020007400650061007200                     ; 14186e1f0  a.k.i. .t.e.a.r.
    .bytes 730020007400680072006f0075006700                     ; 14186e200  s. .t.h.r.o.u.g.
    .bytes 68002000680069007300200065006e00                     ; 14186e210  h. .h.i.s. .e.n.
    .bytes 65006d00690065007300200077006900                     ; 14186e220  e.m.i.e.s. .w.i.
    .bytes 74006800200062006c00610064006500                     ; 14186e230  t.h. .b.l.a.d.e.
    .bytes 640020006700610075006e0074006c00                     ; 14186e240  d. .g.a.u.n.t.l.
    .bytes 6500740073002c002000630072007500                     ; 14186e250  e.t.s.,. .c.r.u.
    .bytes 7300680069006e00670020006b006900                     ; 14186e260  s.h.i.n.g. .k.i.
    .bytes 63006b007300200061006e0064002000                     ; 14186e270  c.k.s. .a.n.d. .
    .bytes 74006800650020007300680061006400                     ; 14186e280  t.h.e. .s.h.a.d.
    .bytes 6f007700200061007200740073002000                     ; 14186e290  o.w. .a.r.t.s. .
    .bytes 6f006600200074006800650020006e00                     ; 14186e2a0  o.f. .t.h.e. .n.
    .bytes 69006e006a0061002e00000000000000                     ; 14186e2b0  i.n.j.a.........
    .bytes 5300700069006e006e0069006e006700                     ; 14186e2c0  S.p.i.n.n.i.n.g.
    .bytes 20004800650065006c00000000000000                     ; 14186e2d0   .H.e.e.l.......
    .bytes 57006800690072006c00200069006e00                     ; 14186e2e0  W.h.i.r.l. .i.n.
    .bytes 74006f00200061002000730070006900                     ; 14186e2f0  t.o. .a. .s.p.i.
    .bytes 6e006e0069006e006700200068006500                     ; 14186e300  n.n.i.n.g. .h.e.
    .bytes 65006c0020006b00690063006b002000                     ; 14186e310  e.l. .k.i.c.k. .
    .bytes 7400680061007400200073006c006100                     ; 14186e320  t.h.a.t. .s.l.a.
    .bytes 73006800650073002000650076006500                     ; 14186e330  s.h.e.s. .e.v.e.
    .bytes 72007900200065006e0065006d007900                     ; 14186e340  r.y. .e.n.e.m.y.
    .bytes 2000610072006f0075006e0064002000                     ; 14186e350   .a.r.o.u.n.d. .
    .bytes 79006f0075002e000000000000000000                     ; 14186e360  y.o.u...........
    .bytes 5253687265646465725f41747461636b                     ; 14186e370  RShredder_Attack
    .bytes 5f436861696e31005253687265646465                     ; 14186e380  _Chain1.RShredde
    .bytes 725f41747461636b5f436861696e3200                     ; 14186e390  r_Attack_Chain2.
    .bytes 5253687265646465725f41747461636b                     ; 14186e3a0  RShredder_Attack
    .bytes 5f436861696e33005253687265646465                     ; 14186e3b0  _Chain3.RShredde
    .bytes 725f41747461636b5f436861696e3400                     ; 14186e3c0  r_Attack_Chain4.
    .bytes 5253687265646465725f446173684174                     ; 14186e3d0  RShredder_DashAt
    .bytes 7461636b000000006576656e743a2f43                     ; 14186e3e0  tack....event:/C
    .bytes 6f6d6261742f424f535345532f536872                     ; 14186e3f0  ombat/BOSSES/Shr
    .bytes 65646465722f436f6d6261745f536872                     ; 14186e400  edder/Combat_Shr
    .bytes 65646465725f536c6173680000000000                     ; 14186e410  edder_Slash.....
    .bytes 6576656e743a2f436f6d6261742f424f                     ; 14186e420  event:/Combat/BO
    .bytes 535345532f53687265646465722f436f                     ; 14186e430  SSES/Shredder/Co
    .bytes 6d6261745f53687265646465725f4b69                     ; 14186e440  mbat_Shredder_Ki
    .bytes 636b0000000000006576656e743a2f43                     ; 14186e450  ck......event:/C
    .bytes 6f6d6261742f424f535345532f536872                     ; 14186e460  ombat/BOSSES/Shr
    .bytes 65646465722f436f6d6261745f536872                     ; 14186e470  edder/Combat_Shr
    .bytes 65646465725f446173685f4174746163                     ; 14186e480  edder_Dash_Attac
    .bytes 6b5f4865617679006576656e743a2f43                     ; 14186e490  k_Heavy.event:/C
    .bytes 6f6d6261742f424f535345532f536872                     ; 14186e4a0  ombat/BOSSES/Shr
    .bytes 65646465722f436f6d6261745f536872                     ; 14186e4b0  edder/Combat_Shr
    .bytes 65646465725f446f75626c6553747269                     ; 14186e4c0  edder_DoubleStri
    .bytes 6b650000000000006275696c643a2f2f                     ; 14186e4d0  ke......build://
    .bytes 456666656374732f4368617261637465                     ; 14186e4e0  Effects/Characte
    .bytes 72732f456e656d6965732f5368726564                     ; 14186e4f0  rs/Enemies/Shred
    .bytes 6465722f53687265646465725f446f75                     ; 14186e500  der/Shredder_Dou
    .bytes 626c65537472696b652f536872656464                     ; 14186e510  bleStrike/Shredd
    .bytes 65725f446f75626c65537472696b652e                     ; 14186e520  er_DoubleStrike.
    .bytes 70667800000000006275696c643a2f2f                     ; 14186e530  pfx.....build://
    .bytes 456666656374732f4368617261637465                     ; 14186e540  Effects/Characte
    .bytes 72732f456e656d6965732f5368726564                     ; 14186e550  rs/Enemies/Shred
    .bytes 6465722f53687265646465725f536861                     ; 14186e560  der/Shredder_Sha
    .bytes 646f774b69636b2f5368726564646572                     ; 14186e570  dowKick/Shredder
    .bytes 5f536861646f774b69636b2e70667800                     ; 14186e580  _ShadowKick.pfx.
    .bytes 6576656e743a2f436f6d6261742f424f                     ; 14186e590  event:/Combat/BO
    .bytes 535345532f53687265646465722f4578                     ; 14186e5a0  SSES/Shredder/Ex
    .bytes 657274696f6e735f5368726564646572                     ; 14186e5b0  ertions_Shredder
    .bytes 5f44616d61676554616b656e00000000                     ; 14186e5c0  _DamageTaken....
    .bytes 5253687265646465725f41747461636b                     ; 14186e5d0  RShredder_Attack
    .bytes 5f436861696e00005368726564646572                     ; 14186e5e0  _Chain..Shredder
    .bytes 5f4869745f5265616374696f6e000000                     ; 14186e5f0  _Hit_Reaction...
    .bytes 53687265646465725f5374756e000000                     ; 14186e600  Shredder_Stun...
    .bytes 53687265646465725f4865726f537069                     ; 14186e610  Shredder_HeroSpi
    .bytes 6e4b69636b0000006576656e743a2f56                     ; 14186e620  nKick...event:/V
    .bytes 4f2f424f535345532f53485245444445                     ; 14186e630  O/BOSSES/SHREDDE
    .bytes 522f5455544f5249414c2f42414e5445                     ; 14186e640  R/TUTORIAL/BANTE
    .bytes 525f5455544f5249414c5f42414e5445                     ; 14186e650  R_TUTORIAL_BANTE
    .bytes 525f484148415f303031000000000000                     ; 14186e660  R_HAHA_001......
    .bytes 6576656e743a2f564f2f424f53534553                     ; 14186e670  event:/VO/BOSSES
    .bytes 2f53485245444445522f424f53532046                     ; 14186e680  /SHREDDER/BOSS F
    .bytes 494748542f42414e5445525f53485245                     ; 14186e690  IGHT/BANTER_SHRE
    .bytes 445f5452414e53315f53485245444445                     ; 14186e6a0  D_TRANS1_SHREDDE
    .bytes 525f41525241595f3030310000000000                     ; 14186e6b0  R_ARRAY_001.....
    .bytes 6576656e743a2f564f2f424f53534553                     ; 14186e6c0  event:/VO/BOSSES
    .bytes 2f53485245444445522f424f53532046                     ; 14186e6d0  /SHREDDER/BOSS F
    .bytes 494748542f42414e5445525f53485245                     ; 14186e6e0  IGHT/BANTER_SHRE
    .bytes 445f5452414e53315f53485245444445                     ; 14186e6f0  D_TRANS1_SHREDDE
    .bytes 525f41525241595f3030330000000000                     ; 14186e700  R_ARRAY_003.....
    .bytes 6576656e743a2f564f2f424f53534553                     ; 14186e710  event:/VO/BOSSES
    .bytes 2f53485245444445522f424f53532046                     ; 14186e720  /SHREDDER/BOSS F
    .bytes 494748542f42414e5445525f53485245                     ; 14186e730  IGHT/BANTER_SHRE
    .bytes 445f474c4f42414c5f58534841444f57                     ; 14186e740  D_GLOBAL_XSHADOW
    .bytes 5f303031000000006162696c69747962                     ; 14186e750  _001....abilityb
    .bytes 7574746f6e5f726562697274685f7368                     ; 14186e760  utton_rebirth_sh
    .bytes 7265646465725f6e6f6e650000000000                     ; 14186e770  redder_none.....
    .bytes 4162696c6974795f4e696e6a615f3030                     ; 14186e780  Ability_Ninja_00
    .bytes 315f536d6f6b65426f6d620000000000                     ; 14186e790  1_SmokeBomb.....
    .bytes 4162696c6974795f436f6d6d6f6e5f30                     ; 14186e7a0  Ability_Common_0
    .bytes 30325f486f6f6b004162696c6974795f                     ; 14186e7b0  02_Hook.Ability_
    .bytes 53687265646465725f536d6f6b65426f                     ; 14186e7c0  Shredder_SmokeBo
    .bytes 6d62000000000000426f73735f536872                     ; 14186e7d0  mb......Boss_Shr
    .bytes 65646465720000007368726564646572                     ; 14186e7e0  edder...shredder
    .bytes 5f736d6f6b655f687564000000000000                     ; 14186e7f0  _smoke_hud......
    sub rsp, 0x28                                                ; 14186e800
    inc byte ptr [rip - 0x80a]                                   ; 14186e804  -> 0x14186e000
    call 0x140883de8                                             ; 14186e80a  -> 0x140883de8 factory Raphael_Attack_Chain
    dec byte ptr [rip - 0x815]                                   ; 14186e80f  -> 0x14186e000
    add rsp, 0x28                                                ; 14186e815
    ret                                                          ; 14186e819
    .bytes 000000000000                                         ; 14186e81a  ......
    sub rsp, 0x28                                                ; 14186e820
    inc byte ptr [rip - 0x82a]                                   ; 14186e824  -> 0x14186e000
    call 0x140884028                                             ; 14186e82a  -> 0x140884028 factory Raphael_Attack_Chain1
    dec byte ptr [rip - 0x835]                                   ; 14186e82f  -> 0x14186e000
    add rsp, 0x28                                                ; 14186e835
    ret                                                          ; 14186e839
    .bytes 000000000000                                         ; 14186e83a  ......
    sub rsp, 0x28                                                ; 14186e840
    inc byte ptr [rip - 0x84a]                                   ; 14186e844  -> 0x14186e000
    call 0x140884f04                                             ; 14186e84a  -> 0x140884f04 factory Raphael_Attack_Chain2
    dec byte ptr [rip - 0x855]                                   ; 14186e84f  -> 0x14186e000
    add rsp, 0x28                                                ; 14186e855
    ret                                                          ; 14186e859
    .bytes 000000000000                                         ; 14186e85a  ......
    sub rsp, 0x28                                                ; 14186e860
    inc byte ptr [rip - 0x86a]                                   ; 14186e864  -> 0x14186e000
    call 0x140885e08                                             ; 14186e86a  -> 0x140885e08 factory Raphael_Attack_Chain3
    dec byte ptr [rip - 0x875]                                   ; 14186e86f  -> 0x14186e000
    add rsp, 0x28                                                ; 14186e875
    ret                                                          ; 14186e879
    .bytes 000000000000                                         ; 14186e87a  ......
    sub rsp, 0x28                                                ; 14186e880
    inc byte ptr [rip - 0x88a]                                   ; 14186e884  -> 0x14186e000
    call 0x140886d90                                             ; 14186e88a  -> 0x140886d90 factory Raphael_Attack_Chain4
    dec byte ptr [rip - 0x895]                                   ; 14186e88f  -> 0x14186e000
    add rsp, 0x28                                                ; 14186e895
    ret                                                          ; 14186e899
    .bytes 000000000000                                         ; 14186e89a  ......
    sub rsp, 0x28                                                ; 14186e8a0
    inc byte ptr [rip - 0x8aa]                                   ; 14186e8a4  -> 0x14186e000
    call 0x14088863c                                             ; 14186e8aa  -> 0x14088863c factory Raphael_DashAttack
    dec byte ptr [rip - 0x8b5]                                   ; 14186e8af  -> 0x14186e000
    add rsp, 0x28                                                ; 14186e8b5
    ret                                                          ; 14186e8b9
    .bytes 000000000000                                         ; 14186e8ba  ......
    sub rsp, 0x28                                                ; 14186e8c0
    inc byte ptr [rip - 0x8ca]                                   ; 14186e8c4  -> 0x14186e000
    call 0x140a06590                                             ; 14186e8ca
    dec byte ptr [rip - 0x8d5]                                   ; 14186e8cf  -> 0x14186e000
    add rsp, 0x28                                                ; 14186e8d5
    ret                                                          ; 14186e8d9
    .bytes 000000000000                                         ; 14186e8da  ......
    sub rsp, 0x28                                                ; 14186e8e0
    inc byte ptr [rip - 0x8ea]                                   ; 14186e8e4  -> 0x14186e000
    call 0x140a057b4                                             ; 14186e8ea
    dec byte ptr [rip - 0x8f5]                                   ; 14186e8ef  -> 0x14186e000
    add rsp, 0x28                                                ; 14186e8f5
    ret                                                          ; 14186e8f9
    .bytes 000000000000                                         ; 14186e8fa  ......
    sub rsp, 0x28                                                ; 14186e900
    inc byte ptr [rip - 0x909]                                   ; 14186e904  -> 0x14186e001
    call 0x140b5bb74                                             ; 14186e90a  -> 0x140b5bb74 factory Boss_Shredder_SpinKick
    dec byte ptr [rip - 0x914]                                   ; 14186e90f  -> 0x14186e001
    add rsp, 0x28                                                ; 14186e915
    ret                                                          ; 14186e919
    .bytes 000000000000                                         ; 14186e91a  ......
  ; ENTRY_14186e920
    lea rax, [rip - 0x357]                                       ; 14186e920  -> 0x14186e5d0 'RShredder_Attack_Chain'
    mov qword ptr [rip - 0x8ce], rax                             ; 14186e927  -> 0x14186e060
    lea rax, [rip - 0x135]                                       ; 14186e92e  -> 0x14186e800
    mov qword ptr [rip - 0x8d4], rax                             ; 14186e935  -> 0x14186e068
    mov rax, qword ptr [rip - 0x277db3]                          ; 14186e93c  -> 0x1415f6b90 behavior registry list head (name -> factory)
    mov qword ptr [rip - 0x8da], rax                             ; 14186e943  -> 0x14186e070
    lea rax, [rip - 0x8f1]                                       ; 14186e94a  -> 0x14186e060
    mov qword ptr [rip - 0x277dc8], rax                          ; 14186e951  -> 0x1415f6b90 behavior registry list head (name -> factory)
    lea rax, [rip - 0x5ef]                                       ; 14186e958  -> 0x14186e370 'RShredder_Attack_Chain1'
    mov qword ptr [rip - 0x8ee], rax                             ; 14186e95f  -> 0x14186e078
    lea rax, [rip - 0x14d]                                       ; 14186e966  -> 0x14186e820
    mov qword ptr [rip - 0x8f4], rax                             ; 14186e96d  -> 0x14186e080
    mov rax, qword ptr [rip - 0x277deb]                          ; 14186e974  -> 0x1415f6b90 behavior registry list head (name -> factory)
    mov qword ptr [rip - 0x8fa], rax                             ; 14186e97b  -> 0x14186e088
    lea rax, [rip - 0x911]                                       ; 14186e982  -> 0x14186e078
    mov qword ptr [rip - 0x277e00], rax                          ; 14186e989  -> 0x1415f6b90 behavior registry list head (name -> factory)
    lea rax, [rip - 0x60f]                                       ; 14186e990  -> 0x14186e388 'RShredder_Attack_Chain2'
    mov qword ptr [rip - 0x90e], rax                             ; 14186e997  -> 0x14186e090
    lea rax, [rip - 0x165]                                       ; 14186e99e  -> 0x14186e840
    mov qword ptr [rip - 0x914], rax                             ; 14186e9a5  -> 0x14186e098
    mov rax, qword ptr [rip - 0x277e23]                          ; 14186e9ac  -> 0x1415f6b90 behavior registry list head (name -> factory)
    mov qword ptr [rip - 0x91a], rax                             ; 14186e9b3  -> 0x14186e0a0
    lea rax, [rip - 0x931]                                       ; 14186e9ba  -> 0x14186e090
    mov qword ptr [rip - 0x277e38], rax                          ; 14186e9c1  -> 0x1415f6b90 behavior registry list head (name -> factory)
    lea rax, [rip - 0x62f]                                       ; 14186e9c8  -> 0x14186e3a0 'RShredder_Attack_Chain3'
    mov qword ptr [rip - 0x92e], rax                             ; 14186e9cf  -> 0x14186e0a8
    lea rax, [rip - 0x17d]                                       ; 14186e9d6  -> 0x14186e860
    mov qword ptr [rip - 0x934], rax                             ; 14186e9dd  -> 0x14186e0b0
    mov rax, qword ptr [rip - 0x277e5b]                          ; 14186e9e4  -> 0x1415f6b90 behavior registry list head (name -> factory)
    mov qword ptr [rip - 0x93a], rax                             ; 14186e9eb  -> 0x14186e0b8
    lea rax, [rip - 0x951]                                       ; 14186e9f2  -> 0x14186e0a8
    mov qword ptr [rip - 0x277e70], rax                          ; 14186e9f9  -> 0x1415f6b90 behavior registry list head (name -> factory)
    lea rax, [rip - 0x64f]                                       ; 14186ea00  -> 0x14186e3b8 'RShredder_Attack_Chain4'
    mov qword ptr [rip - 0x94e], rax                             ; 14186ea07  -> 0x14186e0c0
    lea rax, [rip - 0x195]                                       ; 14186ea0e  -> 0x14186e880
    mov qword ptr [rip - 0x954], rax                             ; 14186ea15  -> 0x14186e0c8
    mov rax, qword ptr [rip - 0x277e93]                          ; 14186ea1c  -> 0x1415f6b90 behavior registry list head (name -> factory)
    mov qword ptr [rip - 0x95a], rax                             ; 14186ea23  -> 0x14186e0d0
    lea rax, [rip - 0x971]                                       ; 14186ea2a  -> 0x14186e0c0
    mov qword ptr [rip - 0x277ea8], rax                          ; 14186ea31  -> 0x1415f6b90 behavior registry list head (name -> factory)
    lea rax, [rip - 0x66f]                                       ; 14186ea38  -> 0x14186e3d0 'RShredder_DashAttack'
    mov qword ptr [rip - 0x96e], rax                             ; 14186ea3f  -> 0x14186e0d8
    lea rax, [rip - 0x1ad]                                       ; 14186ea46  -> 0x14186e8a0
    mov qword ptr [rip - 0x974], rax                             ; 14186ea4d  -> 0x14186e0e0
    mov rax, qword ptr [rip - 0x277ecb]                          ; 14186ea54  -> 0x1415f6b90 behavior registry list head (name -> factory)
    mov qword ptr [rip - 0x97a], rax                             ; 14186ea5b  -> 0x14186e0e8
    lea rax, [rip - 0x991]                                       ; 14186ea62  -> 0x14186e0d8
    mov qword ptr [rip - 0x277ee0], rax                          ; 14186ea69  -> 0x1415f6b90 behavior registry list head (name -> factory)
    lea rax, [rip - 0x48f]                                       ; 14186ea70  -> 0x14186e5e8 'Shredder_Hit_Reaction'
    mov qword ptr [rip - 0x98e], rax                             ; 14186ea77  -> 0x14186e0f0
    lea rax, [rip - 0x1c5]                                       ; 14186ea7e  -> 0x14186e8c0
    mov qword ptr [rip - 0x994], rax                             ; 14186ea85  -> 0x14186e0f8
    mov rax, qword ptr [rip - 0x277f03]                          ; 14186ea8c  -> 0x1415f6b90 behavior registry list head (name -> factory)
    mov qword ptr [rip - 0x99a], rax                             ; 14186ea93  -> 0x14186e100
    lea rax, [rip - 0x9b1]                                       ; 14186ea9a  -> 0x14186e0f0
    mov qword ptr [rip - 0x277f18], rax                          ; 14186eaa1  -> 0x1415f6b90 behavior registry list head (name -> factory)
    lea rax, [rip - 0x4af]                                       ; 14186eaa8  -> 0x14186e600 'Shredder_Stun'
    mov qword ptr [rip - 0x9ae], rax                             ; 14186eaaf  -> 0x14186e108
    lea rax, [rip - 0x1dd]                                       ; 14186eab6  -> 0x14186e8e0
    mov qword ptr [rip - 0x9b4], rax                             ; 14186eabd  -> 0x14186e110
    mov rax, qword ptr [rip - 0x277f3b]                          ; 14186eac4  -> 0x1415f6b90 behavior registry list head (name -> factory)
    mov qword ptr [rip - 0x9ba], rax                             ; 14186eacb  -> 0x14186e118
    lea rax, [rip - 0x9d1]                                       ; 14186ead2  -> 0x14186e108
    mov qword ptr [rip - 0x277f50], rax                          ; 14186ead9  -> 0x1415f6b90 behavior registry list head (name -> factory)
    lea rax, [rip - 0x4d7]                                       ; 14186eae0  -> 0x14186e610 'Shredder_HeroSpinKick'
    mov qword ptr [rip - 0x9ce], rax                             ; 14186eae7  -> 0x14186e120
    lea rax, [rip - 0x1f5]                                       ; 14186eaee  -> 0x14186e900
    mov qword ptr [rip - 0x9d4], rax                             ; 14186eaf5  -> 0x14186e128
    mov rax, qword ptr [rip - 0x277f73]                          ; 14186eafc  -> 0x1415f6b90 behavior registry list head (name -> factory)
    mov qword ptr [rip - 0x9da], rax                             ; 14186eb03  -> 0x14186e130
    lea rax, [rip - 0x9f1]                                       ; 14186eb0a  -> 0x14186e120
    mov qword ptr [rip - 0x277f88], rax                          ; 14186eb11  -> 0x1415f6b90 behavior registry list head (name -> factory)
    lea rax, [rip - 0x96f]                                       ; 14186eb18  -> 0x14186e1b0
    mov qword ptr [rip - 0x9de], rax                             ; 14186eb1f  -> 0x14186e148
    lea rax, [rip - 0x86d]                                       ; 14186eb26  -> 0x14186e2c0
    mov qword ptr [rip - 0x9dc], rax                             ; 14186eb2d  -> 0x14186e158
    lea rax, [rip - 0x85b]                                       ; 14186eb34  -> 0x14186e2e0
    mov qword ptr [rip - 0x9da], rax                             ; 14186eb3b  -> 0x14186e168
    jmp 0x140f6ac80                                              ; 14186eb42
    .bytes 000000000000000000                                   ; 14186eb47  .........
  ; ENTRY_14186eb50
    pushfq                                                       ; 14186eb50
    lea rdx, [rip - 0x6c49b8]                                    ; 14186eb51  -> 0x1411aa1a0 'Raphael_Attack_Chain1'
    cmp byte ptr [rip - 0xb5f], 0                                ; 14186eb58  -> 0x14186e000
    je 0x14186eb68                                               ; 14186eb5f
    lea rdx, [rip - 0x7f8]                                       ; 14186eb61  -> 0x14186e370 'RShredder_Attack_Chain1'
  ; L_14186eb68
    popfq                                                        ; 14186eb68
    jmp 0x140883e59                                              ; 14186eb69
    .bytes 0000                                                 ; 14186eb6e  ..
  ; ENTRY_14186eb70
    pushfq                                                       ; 14186eb70
    lea rcx, [rip - 0x6c49f0]                                    ; 14186eb71  -> 0x1411aa188 'Raphael_Attack_Chain2'
    cmp byte ptr [rip - 0xb7f], 0                                ; 14186eb78  -> 0x14186e000
    je 0x14186eb88                                               ; 14186eb7f
    lea rcx, [rip - 0x800]                                       ; 14186eb81  -> 0x14186e388 'RShredder_Attack_Chain2'
  ; L_14186eb88
    popfq                                                        ; 14186eb88
    jmp 0x140883eb4                                              ; 14186eb89
    .bytes 0000                                                 ; 14186eb8e  ..
  ; ENTRY_14186eb90
    pushfq                                                       ; 14186eb90
    lea rcx, [rip - 0x6c4a28]                                    ; 14186eb91  -> 0x1411aa170 'Raphael_Attack_Chain3'
    cmp byte ptr [rip - 0xb9f], 0                                ; 14186eb98  -> 0x14186e000
    je 0x14186eba8                                               ; 14186eb9f
    lea rcx, [rip - 0x808]                                       ; 14186eba1  -> 0x14186e3a0 'RShredder_Attack_Chain3'
  ; L_14186eba8
    popfq                                                        ; 14186eba8
    jmp 0x140883f05                                              ; 14186eba9
    .bytes 0000                                                 ; 14186ebae  ..
  ; ENTRY_14186ebb0
    pushfq                                                       ; 14186ebb0
    lea rcx, [rip - 0x6c4a60]                                    ; 14186ebb1  -> 0x1411aa158 'Raphael_Attack_Chain4'
    cmp byte ptr [rip - 0xbbf], 0                                ; 14186ebb8  -> 0x14186e000
    je 0x14186ebc8                                               ; 14186ebbf
    lea rcx, [rip - 0x810]                                       ; 14186ebc1  -> 0x14186e3b8 'RShredder_Attack_Chain4'
  ; L_14186ebc8
    popfq                                                        ; 14186ebc8
    jmp 0x140883f56                                              ; 14186ebc9
    .bytes 0000                                                 ; 14186ebce  ..
  ; ENTRY_14186ebd0
    pushfq                                                       ; 14186ebd0
    lea rcx, [rip - 0x6c4a98]                                    ; 14186ebd1  -> 0x1411aa140 'Raphael_DashAttack'
    cmp byte ptr [rip - 0xbdf], 0                                ; 14186ebd8  -> 0x14186e000
    je 0x14186ebe8                                               ; 14186ebdf
    lea rcx, [rip - 0x818]                                       ; 14186ebe1  -> 0x14186e3d0 'RShredder_DashAttack'
  ; L_14186ebe8
    popfq                                                        ; 14186ebe8
    jmp 0x140883fa7                                              ; 14186ebe9
    .bytes 0000                                                 ; 14186ebee  ..
  ; ENTRY_14186ebf0
    pushfq                                                       ; 14186ebf0
    lea rcx, [rip - 0x6c4d50]                                    ; 14186ebf1  -> 0x1411a9ea8 'event:/Combat/TURTLES/RAPH/Combat_Raph_Swing_Light'
    cmp byte ptr [rip - 0xbff], 0                                ; 14186ebf8  -> 0x14186e000
    je 0x14186ec08                                               ; 14186ebff
    lea rcx, [rip - 0x820]                                       ; 14186ec01  -> 0x14186e3e8 'event:/Combat/BOSSES/Shredder/Combat_Shredder_Slash'
  ; L_14186ec08
    popfq                                                        ; 14186ec08
    jmp 0x14088487f                                              ; 14186ec09
    .bytes 0000                                                 ; 14186ec0e  ..
  ; ENTRY_14186ec10
    pushfq                                                       ; 14186ec10
    lea rcx, [rip - 0x6c4d70]                                    ; 14186ec11  -> 0x1411a9ea8 'event:/Combat/TURTLES/RAPH/Combat_Raph_Swing_Light'
    cmp byte ptr [rip - 0xc1f], 0                                ; 14186ec18  -> 0x14186e000
    je 0x14186ec28                                               ; 14186ec1f
    lea rcx, [rip - 0x808]                                       ; 14186ec21  -> 0x14186e420 'event:/Combat/BOSSES/Shredder/Combat_Shredder_Kick'
  ; L_14186ec28
    popfq                                                        ; 14186ec28
    jmp 0x140885770                                              ; 14186ec29
    .bytes 0000                                                 ; 14186ec2e  ..
  ; ENTRY_14186ec30
    pushfq                                                       ; 14186ec30
    lea rcx, [rip - 0x6c4d90]                                    ; 14186ec31  -> 0x1411a9ea8 'event:/Combat/TURTLES/RAPH/Combat_Raph_Swing_Light'
    cmp byte ptr [rip - 0xc3f], 0                                ; 14186ec38  -> 0x14186e000
    je 0x14186ec48                                               ; 14186ec3f
    lea rcx, [rip - 0x7f0]                                       ; 14186ec41  -> 0x14186e458 'event:/Combat/BOSSES/Shredder/Combat_Shredder_Dash_Attack_Heavy'
  ; L_14186ec48
    popfq                                                        ; 14186ec48
    jmp 0x1408864ee                                              ; 14186ec49
    .bytes 0000                                                 ; 14186ec4e  ..
  ; ENTRY_14186ec50
    pushfq                                                       ; 14186ec50
    lea rcx, [rip - 0x6c4d40]                                    ; 14186ec51  -> 0x1411a9f18 'event:/Combat/TURTLES/RAPH/Combat_Raph_Swing_Heavy'
    cmp byte ptr [rip - 0xc5f], 0                                ; 14186ec58  -> 0x14186e000
    je 0x14186ec68                                               ; 14186ec5f
    lea rcx, [rip - 0x7d0]                                       ; 14186ec61  -> 0x14186e498 'event:/Combat/BOSSES/Shredder/Combat_Shredder_DoubleStrike'
  ; L_14186ec68
    popfq                                                        ; 14186ec68
    jmp 0x140887c9f                                              ; 14186ec69
    .bytes 0000                                                 ; 14186ec6e  ..
  ; ENTRY_14186ec70
    pushfq                                                       ; 14186ec70
    lea rax, [rip - 0x6c4cb8]                                    ; 14186ec71  -> 0x1411a9fc0 'build://Effects/Characters/Turtles/Raphael/BasicAttacks/Raphael_Attack_04/Raphael_Attack_04b.pfx'
    cmp byte ptr [rip - 0xc7f], 0                                ; 14186ec78  -> 0x14186e000
    je 0x14186ec88                                               ; 14186ec7f
    lea rax, [rip - 0x7b0]                                       ; 14186ec81  -> 0x14186e4d8 'build://Effects/Characters/Enemies/Shredder/Shredder_DoubleStrike/Shredder_DoubleStrike.pfx'
  ; L_14186ec88
    popfq                                                        ; 14186ec88
    jmp 0x1408872d3                                              ; 14186ec89
    .bytes 0000                                                 ; 14186ec8e  ..
  ; ENTRY_14186ec90
    pushfq                                                       ; 14186ec90
    lea rax, [rip - 0x6c4d48]                                    ; 14186ec91  -> 0x1411a9f50 'build://Effects/Characters/Turtles/Raphael/BasicAttacks/Raphael_Attack_04/Raphael_Attack_04a.pfx'
    cmp byte ptr [rip - 0xc9f], 0                                ; 14186ec98  -> 0x14186e000
    je 0x14186eca8                                               ; 14186ec9f
    lea rax, [rip - 0x7d0]                                       ; 14186eca1  -> 0x14186e4d8 'build://Effects/Characters/Enemies/Shredder/Shredder_DoubleStrike/Shredder_DoubleStrike.pfx'
  ; L_14186eca8
    popfq                                                        ; 14186eca8
    jmp 0x140887997                                              ; 14186eca9
    .bytes 0000                                                 ; 14186ecae  ..
  ; ENTRY_14186ecb0
    pushfq                                                       ; 14186ecb0
    lea rcx, [rip - 0x6c4e10]                                    ; 14186ecb1  -> 0x1411a9ea8 'event:/Combat/TURTLES/RAPH/Combat_Raph_Swing_Light'
    cmp byte ptr [rip - 0xcbf], 0                                ; 14186ecb8  -> 0x14186e000
    je 0x14186ecc8                                               ; 14186ecbf
    lea rcx, [rip - 0x8a8]                                       ; 14186ecc1  -> 0x14186e420 'event:/Combat/BOSSES/Shredder/Combat_Shredder_Kick'
  ; L_14186ecc8
    popfq                                                        ; 14186ecc8
    jmp 0x140888cc7                                              ; 14186ecc9
    .bytes 0000                                                 ; 14186ecce  ..
  ; ENTRY_14186ecd0
    pushfq                                                       ; 14186ecd0
    lea rcx, [rip - 0x6c4e30]                                    ; 14186ecd1  -> 0x1411a9ea8 'event:/Combat/TURTLES/RAPH/Combat_Raph_Swing_Light'
    cmp byte ptr [rip - 0xcdf], 0                                ; 14186ecd8  -> 0x14186e000
    je 0x14186ece8                                               ; 14186ecdf
    lea rcx, [rip - 0x8c8]                                       ; 14186ece1  -> 0x14186e420 'event:/Combat/BOSSES/Shredder/Combat_Shredder_Kick'
  ; L_14186ece8
    popfq                                                        ; 14186ece8
    jmp 0x140888f7d                                              ; 14186ece9
    .bytes 0000                                                 ; 14186ecee  ..
  ; ENTRY_14186ecf0
    pushfq                                                       ; 14186ecf0
    lea rax, [rip - 0x6c50a8]                                    ; 14186ecf1  -> 0x1411a9c50 'build://Effects/Characters/Turtles/Raphael/DashAttack/Raphael_DashAttack.pfx'
    cmp byte ptr [rip - 0xcff], 0                                ; 14186ecf8  -> 0x14186e000
    je 0x14186ed08                                               ; 14186ecff
    lea rax, [rip - 0x7d0]                                       ; 14186ed01  -> 0x14186e538 'build://Effects/Characters/Enemies/Shredder/Shredder_ShadowKick/Shredder_ShadowKick.pfx'
  ; L_14186ed08
    popfq                                                        ; 14186ed08
    jmp 0x140888e79                                              ; 14186ed09
    .bytes 0000                                                 ; 14186ed0e  ..
  ; ENTRY_14186ed10
    pushfq                                                       ; 14186ed10
    lea rax, [rip - 0x6acb50]                                    ; 14186ed11  -> 0x1411c21c8 'event:/Combat/TURTLES/RAPH/Exertion_Raph_Stunned'
    cmp byte ptr [rip - 0xd1f], 0                                ; 14186ed18  -> 0x14186e000
    je 0x14186ed28                                               ; 14186ed1f
    lea rax, [rip - 0x798]                                       ; 14186ed21  -> 0x14186e590 'event:/Combat/BOSSES/Shredder/Exertions_Shredder_DamageTaken'
  ; L_14186ed28
    popfq                                                        ; 14186ed28
    jmp 0x140a05ca4                                              ; 14186ed29
    .bytes 0000                                                 ; 14186ed2e  ..
  ; ENTRY_14186ed30
    pushfq                                                       ; 14186ed30
    lea rax, [rip - 0x6ac620]                                    ; 14186ed31  -> 0x1411c2718 'event:/Combat/TURTLES/RAPH/Exertion_Raph_DamageTaken'
    cmp byte ptr [rip - 0xd3f], 0                                ; 14186ed38  -> 0x14186e000
    je 0x14186ed48                                               ; 14186ed3f
    lea rax, [rip - 0x7b8]                                       ; 14186ed41  -> 0x14186e590 'event:/Combat/BOSSES/Shredder/Exertions_Shredder_DamageTaken'
  ; L_14186ed48
    popfq                                                        ; 14186ed48
    jmp 0x140a06a83                                              ; 14186ed49
    .bytes 0000                                                 ; 14186ed4e  ..
  ; ENTRY_14186ed50
    mov qword ptr [rbp + 0x2b8], 0xa02000                        ; 14186ed50
    cmp byte ptr [rip - 0xd61], 0                                ; 14186ed5b  -> 0x14186e001
    je 0x140b5bd14                                               ; 14186ed62
    lea rax, [rip - 0x11c0e27]                                   ; 14186ed68  -> 0x1406adf48 hero stat fn 0x1a (special damage)
    mov qword ptr [rbp + 0x260], rax                             ; 14186ed6f
    mov byte ptr [rbp + 0x268], 4                                ; 14186ed76
    mov eax, dword ptr [rip - 0xd6f]                             ; 14186ed7d  -> 0x14186e014
    mov dword ptr [rbp + 0x270], eax                             ; 14186ed83
    mov dword ptr [rbp + 0x274], 0                               ; 14186ed89
    mov byte ptr [rbp + 0x278], 1                                ; 14186ed93
    mov qword ptr [rbp + 0x2b8], 0x2004                          ; 14186ed9a
    jmp 0x140b5bd14                                              ; 14186eda5
    .bytes 000000000000                                         ; 14186edaa  ......
  ; ENTRY_14186edb0
    movss xmm1, dword ptr [rip - 0x600f8c]                       ; 14186edb0  -> 0x14126de2c
    pushfq                                                       ; 14186edb8
    cmp byte ptr [rip - 0xdbf], 0                                ; 14186edb9  -> 0x14186e001
    je 0x14186edca                                               ; 14186edc0
    mulss xmm1, dword ptr [rip - 0xdba]                          ; 14186edc2  -> 0x14186e010
  ; L_14186edca
    popfq                                                        ; 14186edca
    jmp 0x140b5bd8d                                              ; 14186edcb
  ; ENTRY_14186edd0
    movss xmm1, dword ptr [rip - 0x60138c]                       ; 14186edd0  -> 0x14126da4c
    pushfq                                                       ; 14186edd8
    cmp byte ptr [rip - 0xddf], 0                                ; 14186edd9  -> 0x14186e001
    je 0x14186edea                                               ; 14186ede0
    mulss xmm1, dword ptr [rip - 0xdda]                          ; 14186ede2  -> 0x14186e010
  ; L_14186edea
    popfq                                                        ; 14186edea
    jmp 0x140b5be23                                              ; 14186edeb
  ; ENTRY_14186edf0
    movss xmm1, dword ptr [rip - 0x6013ac]                       ; 14186edf0  -> 0x14126da4c
    pushfq                                                       ; 14186edf8
    cmp byte ptr [rip - 0xdff], 0                                ; 14186edf9  -> 0x14186e001
    je 0x14186ee0a                                               ; 14186ee00
    mulss xmm1, dword ptr [rip - 0xdfa]                          ; 14186ee02  -> 0x14186e010
  ; L_14186ee0a
    popfq                                                        ; 14186ee0a
    jmp 0x140b5be9d                                              ; 14186ee0b
  ; ENTRY_14186ee10
    movss xmm1, dword ptr [rip - 0x6013cc]                       ; 14186ee10  -> 0x14126da4c
    pushfq                                                       ; 14186ee18
    cmp byte ptr [rip - 0xe1f], 0                                ; 14186ee19  -> 0x14186e001
    je 0x14186ee2a                                               ; 14186ee20
    mulss xmm1, dword ptr [rip - 0xe1a]                          ; 14186ee22  -> 0x14186e010
  ; L_14186ee2a
    popfq                                                        ; 14186ee2a
    jmp 0x140b5bf18                                              ; 14186ee2b
  ; ENTRY_14186ee30
    movss xmm1, dword ptr [rip - 0x6013ec]                       ; 14186ee30  -> 0x14126da4c
    pushfq                                                       ; 14186ee38
    cmp byte ptr [rip - 0xe3f], 0                                ; 14186ee39  -> 0x14186e001
    je 0x14186ee4a                                               ; 14186ee40
    mulss xmm1, dword ptr [rip - 0xe3a]                          ; 14186ee42  -> 0x14186e010
  ; L_14186ee4a
    popfq                                                        ; 14186ee4a
    jmp 0x140b5bf9a                                              ; 14186ee4b
  ; ENTRY_14186ee50
    movss xmm1, dword ptr [rip - 0x60116c]                       ; 14186ee50  -> 0x14126dcec
    pushfq                                                       ; 14186ee58
    cmp byte ptr [rip - 0xe5f], 0                                ; 14186ee59  -> 0x14186e001
    je 0x14186ee6a                                               ; 14186ee60
    mulss xmm1, dword ptr [rip - 0xe5a]                          ; 14186ee62  -> 0x14186e010
  ; L_14186ee6a
    popfq                                                        ; 14186ee6a
    jmp 0x140b5c078                                              ; 14186ee6b
  ; L_14186ee70
    mov eax, dword ptr [rsi + 0xa0]                              ; 14186ee70
    lea r15, [r14 + 0x28]                                        ; 14186ee76
    mov edx, dword ptr [rip - 0xe60]                             ; 14186ee7a  -> 0x14186e020
    lea r8, [rbp + 0xf0]                                         ; 14186ee80
    .bytes 498bcf                                               ; 14186ee87  mov rcx, r15  (exact original encoding)
    mov dword ptr [rbp + 0xf0], eax                              ; 14186ee8a
    .bytes 448bcb                                               ; 14186ee90  mov r9d, ebx  (exact original encoding)
    call 0x140d3c0b4                                             ; 14186ee93
    cmp byte ptr [rsi + 0xe0], 0                                 ; 14186ee98
    jne 0x14186eea6                                              ; 14186ee9f
    movaps xmm2, xmm6                                            ; 14186eea1
    jmp 0x14186eea9                                              ; 14186eea4
  ; L_14186eea6
    xorps xmm2, xmm2                                             ; 14186eea6
  ; L_14186eea9
    mov edx, dword ptr [rip - 0xe8b]                             ; 14186eea9  -> 0x14186e024
    .bytes 448bcb                                               ; 14186eeaf  mov r9d, ebx  (exact original encoding)
    .bytes 498bcf                                               ; 14186eeb2  mov rcx, r15  (exact original encoding)
    call 0x140d3c058                                             ; 14186eeb5
    mov edx, dword ptr [rip - 0xe98]                             ; 14186eeba  -> 0x14186e028
    .bytes 448bcb                                               ; 14186eec0  mov r9d, ebx  (exact original encoding)
    movaps xmm2, xmm6                                            ; 14186eec3
    .bytes 498bcf                                               ; 14186eec6  mov rcx, r15  (exact original encoding)
    call 0x140d3c058                                             ; 14186eec9
    mov r9, qword ptr [rdi + 8]                                  ; 14186eece
    sub rdi, qword ptr [r9 + 0x298]                              ; 14186eed2
    mov ecx, dword ptr [r9 + 0x7c]                               ; 14186eed9
    .bytes 488bc7                                               ; 14186eedd  mov rax, rdi  (exact original encoding)
    cqo                                                          ; 14186eee0
    idiv rcx                                                     ; 14186eee2
    mov edx, dword ptr [r9 + 0x78]                               ; 14186eee5
    .bytes 4c8bc0                                               ; 14186eee9  mov r8, rax  (exact original encoding)
    mov rax, qword ptr [rip - 0x1c225b]                          ; 14186eeec  -> 0x1416acc98
    mov rcx, qword ptr [rax + 0x58]                              ; 14186eef3
    mov rax, qword ptr [rax + 0x10]                              ; 14186eef7
    add r8d, dword ptr [rcx + rdx*4]                             ; 14186eefb
    mov edx, dword ptr [rax + r8*8]                              ; 14186eeff
    shr rdx, 0xb                                                 ; 14186ef03
    test bl, dl                                                  ; 14186ef07
    je 0x14186ef10                                               ; 14186ef09
    movaps xmm2, xmm6                                            ; 14186ef0b
    jmp 0x14186ef13                                              ; 14186ef0e
  ; L_14186ef10
    xorps xmm2, xmm2                                             ; 14186ef10
  ; L_14186ef13
    mov edx, dword ptr [rip - 0xeed]                             ; 14186ef13  -> 0x14186e02c
    .bytes 448bcb                                               ; 14186ef19  mov r9d, ebx  (exact original encoding)
    .bytes 498bcf                                               ; 14186ef1c  mov rcx, r15  (exact original encoding)
    call 0x140d3c058                                             ; 14186ef1f
    test r12b, r12b                                              ; 14186ef24
    je 0x14072ea8a                                               ; 14186ef27
    mov edx, dword ptr [rip - 0xf03]                             ; 14186ef2d  -> 0x14186e030
    jmp 0x14072ea7c                                              ; 14186ef33
    .bytes 00000000000000000000000000000000                     ; 14186ef38  ................
    .bytes 0000000000000000                                     ; 14186ef48  ........
  ; ENTRY_14186ef50
    cmp eax, 2                                                   ; 14186ef50
    je 0x14186ee70                                               ; 14186ef53
    cmp eax, ebx                                                 ; 14186ef59
    jne 0x14072ea8d                                              ; 14186ef5b
    jmp 0x14072e3ec                                              ; 14186ef61
    .bytes 00000000000000000000                                 ; 14186ef66  ..........
  ; ENTRY_14186ef70
    cmp ebx, 1                                                   ; 14186ef70
    jne 0x14186efb9                                              ; 14186ef73
    call qword ptr [rip - 0x902a2b]                              ; 14186ef75  -> 0x140f6c550 rand (import)
    xor edx, edx                                                 ; 14186ef7b
    mov ecx, 4                                                   ; 14186ef7d
    div ecx                                                      ; 14186ef82
    lea rdi, [rip - 0x963]                                       ; 14186ef84  -> 0x14186e628 'event:/VO/BOSSES/SHREDDER/TUTORIAL/BANTER_TUTORIAL_BANTER_HAHA_001'
    cmp edx, 0                                                   ; 14186ef8b
    je 0x14186efb4                                               ; 14186ef8e
    lea rdi, [rip - 0x927]                                       ; 14186ef90  -> 0x14186e670 'event:/VO/BOSSES/SHREDDER/BOSS FIGHT/BANTER_SHRED_TRANS1_SHREDDER_ARRAY_001'
    cmp edx, 1                                                   ; 14186ef97
    je 0x14186efb4                                               ; 14186ef9a
    lea rdi, [rip - 0x8e3]                                       ; 14186ef9c  -> 0x14186e6c0 'event:/VO/BOSSES/SHREDDER/BOSS FIGHT/BANTER_SHRED_TRANS1_SHREDDER_ARRAY_003'
    cmp edx, 2                                                   ; 14186efa3
    je 0x14186efb4                                               ; 14186efa6
    lea rdi, [rip - 0x89f]                                       ; 14186efa8  -> 0x14186e710 'event:/VO/BOSSES/SHREDDER/BOSS FIGHT/BANTER_SHRED_GLOBAL_XSHADOW_001'
    cmp edx, 3                                                   ; 14186efaf
    je 0x14186efb4                                               ; 14186efb2
  ; L_14186efb4
    jmp 0x140655ca0                                              ; 14186efb4
  ; L_14186efb9
    jmp 0x140655ca0                                              ; 14186efb9
    .bytes 0000                                                 ; 14186efbe  ..
  ; ENTRY_14186efc0
    cmp ecx, 0x55058dca                                          ; 14186efc0
    je 0x14186efe4                                               ; 14186efc6
    cmp ecx, 0x15ecd5fb                                          ; 14186efc8
    je 0x14186efec                                               ; 14186efce
    cmp ecx, 0xac4af389                                          ; 14186efd0
    je 0x14186eff4                                               ; 14186efd6
    push rbx                                                     ; 14186efd8
    sub rsp, 0x20                                                ; 14186efd9
    mov ebx, ecx                                                 ; 14186efdd
    jmp 0x140742794                                              ; 14186efdf
  ; L_14186efe4
    lea rax, [rip - 0xeab]                                       ; 14186efe4  -> 0x14186e140
    ret                                                          ; 14186efeb
  ; L_14186efec
    lea rax, [rip - 0xea3]                                       ; 14186efec  -> 0x14186e150
    ret                                                          ; 14186eff3
  ; L_14186eff4
    lea rax, [rip - 0xe9b]                                       ; 14186eff4  -> 0x14186e160
    ret                                                          ; 14186effb
    .bytes 00000000                                             ; 14186effc  ....
  ; ENTRY_14186f000
    mov r14, qword ptr [rdx + 0x38]                              ; 14186f000
    test r14, r14                                                ; 14186f004
    je 0x14186f10c                                               ; 14186f007
    push rcx                                                     ; 14186f00d
    push rdx                                                     ; 14186f00e
    push r8                                                      ; 14186f00f
    push r9                                                      ; 14186f011
    push r10                                                     ; 14186f013
    push r11                                                     ; 14186f015
    cmp qword ptr [r14], 0                                       ; 14186f017
    je 0x14186f102                                               ; 14186f01b
    mov rax, qword ptr [r14]                                     ; 14186f021
    lea rcx, [rip - 0x8ab]                                       ; 14186f024  -> 0x14186e780 'Ability_Ninja_001_SmokeBomb'
  ; L_14186f02b
    mov r8b, byte ptr [rax]                                      ; 14186f02b
    cmp r8b, byte ptr [rcx]                                      ; 14186f02e
    jne 0x14186f040                                              ; 14186f031
    test r8b, r8b                                                ; 14186f033
    je 0x14186f063                                               ; 14186f036
    inc rax                                                      ; 14186f038
    inc rcx                                                      ; 14186f03b
    jmp 0x14186f02b                                              ; 14186f03e
  ; L_14186f040
    mov rax, qword ptr [r14]                                     ; 14186f040
    lea rcx, [rip - 0x8aa]                                       ; 14186f043  -> 0x14186e7a0 'Ability_Common_002_Hook'
  ; L_14186f04a
    mov r8b, byte ptr [rax]                                      ; 14186f04a
    cmp r8b, byte ptr [rcx]                                      ; 14186f04d
    jne 0x14186f102                                              ; 14186f050
    test r8b, r8b                                                ; 14186f056
    je 0x14186f063                                               ; 14186f059
    inc rax                                                      ; 14186f05b
    inc rcx                                                      ; 14186f05e
    jmp 0x14186f04a                                              ; 14186f061
  ; L_14186f063
    lea rcx, [rbp + 0x10]                                        ; 14186f063
    call 0x14056bd48                                             ; 14186f067
    test rax, rax                                                ; 14186f06c
    je 0x14186f102                                               ; 14186f06f
    cmp dword ptr [rax + 0x78], 0xe1efc639                       ; 14186f075
    jne 0x14186f102                                              ; 14186f07c
    lea rcx, [rip - 0xf19]                                       ; 14186f082  -> 0x14186e170
    mov rax, qword ptr [r14]                                     ; 14186f089
    mov qword ptr [rcx], rax                                     ; 14186f08c
    mov rax, qword ptr [r14 + 8]                                 ; 14186f08f
    mov qword ptr [rcx + 8], rax                                 ; 14186f093
    mov rax, qword ptr [r14 + 0x10]                              ; 14186f097
    mov qword ptr [rcx + 0x10], rax                              ; 14186f09b
    mov rax, qword ptr [r14 + 0x18]                              ; 14186f09f
    mov qword ptr [rcx + 0x18], rax                              ; 14186f0a3
    mov rax, qword ptr [r14 + 0x20]                              ; 14186f0a7
    mov qword ptr [rcx + 0x20], rax                              ; 14186f0ab
    mov rax, qword ptr [r14 + 0x28]                              ; 14186f0af
    mov qword ptr [rcx + 0x28], rax                              ; 14186f0b3
    mov rax, qword ptr [r14 + 0x30]                              ; 14186f0b7
    mov qword ptr [rcx + 0x30], rax                              ; 14186f0bb
    mov rax, qword ptr [r14 + 0x38]                              ; 14186f0bf
    mov qword ptr [rcx + 0x38], rax                              ; 14186f0c3
    lea rax, [rip - 0x916]                                       ; 14186f0c7  -> 0x14186e7b8 'Ability_Shredder_SmokeBomb'
    mov qword ptr [rcx], rax                                     ; 14186f0ce
    lea rax, [rip - 0x900]                                       ; 14186f0d1  -> 0x14186e7d8 'Boss_Shredder'
    mov qword ptr [rcx + 0x18], rax                              ; 14186f0d8
    lea rax, [rip - 0x8fb]                                       ; 14186f0dc  -> 0x14186e7e8 'shredder_smoke_hud'
    mov qword ptr [rcx + 0x20], rax                              ; 14186f0e3
    mov qword ptr [rcx + 0x28], rax                              ; 14186f0e7
    mov r14, rcx                                                 ; 14186f0eb
    pop r11                                                      ; 14186f0ee
    pop r10                                                      ; 14186f0f0
    pop r9                                                       ; 14186f0f2
    pop r8                                                       ; 14186f0f4
    pop rdx                                                      ; 14186f0f6
    pop rcx                                                      ; 14186f0f7
    mov qword ptr [rsp + 0x28], r14                              ; 14186f0f8
    jmp 0x140683670                                              ; 14186f0fd
  ; L_14186f102
    pop r11                                                      ; 14186f102
    pop r10                                                      ; 14186f104
    pop r9                                                       ; 14186f106
    pop r8                                                       ; 14186f108
    pop rdx                                                      ; 14186f10a
    pop rcx                                                      ; 14186f10b
  ; L_14186f10c
    mov qword ptr [rsp + 0x28], r14                              ; 14186f10c
    jmp 0x140683670                                              ; 14186f111
    .bytes 00000000000000000000                                 ; 14186f116  ..........
    push rbx                                                     ; 14186f120
    push rsi                                                     ; 14186f121
    sub rsp, 0x38                                                ; 14186f122
    mov rbx, rcx                                                 ; 14186f126
    mov rsi, rdx                                                 ; 14186f129
    call 0x1406b19a4                                             ; 14186f12c  -> 0x1406b19a4 actor condition eval
    test al, al                                                  ; 14186f131
    jne 0x14186f15d                                              ; 14186f133
    lea rcx, [rbx + 0x30]                                        ; 14186f135
    lea rdx, [rsp + 0x20]                                        ; 14186f139
    mov r8, rsi                                                  ; 14186f13e
    xor r9d, r9d                                                 ; 14186f141
    mov qword ptr [rsp + 0x20], 0                                ; 14186f144
    call 0x1406b2580                                             ; 14186f14d
    cmp dword ptr [rsp + 0x20], 0xe1efc639                       ; 14186f152
    sete al                                                      ; 14186f15a
  ; L_14186f15d
    add rsp, 0x38                                                ; 14186f15d
    pop rsi                                                      ; 14186f161
    pop rbx                                                      ; 14186f162
    ret                                                          ; 14186f163
    .bytes 000000000000000000000000                             ; 14186f164  ............
  ; ENTRY_14186f170
    mov r9, rax                                                  ; 14186f170
    mov byte ptr [rbp - 0x68], 0                                 ; 14186f173
    mov rcx, qword ptr [rax]                                     ; 14186f177
    mov rdx, qword ptr [rip - 0x709849]                          ; 14186f17a  -> 0x141165938
    mov qword ptr [rip - 0x1148], rdx                            ; 14186f181  -> 0x14186e040
    mov rdx, qword ptr [rip - 0x70984f]                          ; 14186f188  -> 0x141165940
    mov qword ptr [rip - 0x114e], rdx                            ; 14186f18f  -> 0x14186e048
    lea rdx, [rip - 0x7d]                                        ; 14186f196  -> 0x14186f120
    mov qword ptr [rip - 0x1154], rdx                            ; 14186f19d  -> 0x14186e050
    lea rdx, [rip - 0x1163]                                      ; 14186f1a4  -> 0x14186e048
    mov qword ptr [rcx], rdx                                     ; 14186f1ab
    jmp 0x1406ad1a7                                              ; 14186f1ae
    .bytes 00000000000000000000000000000000                     ; 14186f1b3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f1c3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f1d3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f1e3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f1f3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f203  ................
    .bytes 00000000000000000000000000000000                     ; 14186f213  ................
    .bytes 00000000000000000000000000000000                     ; 14186f223  ................
    .bytes 00000000000000000000000000000000                     ; 14186f233  ................
    .bytes 00000000000000000000000000000000                     ; 14186f243  ................
    .bytes 00000000000000000000000000000000                     ; 14186f253  ................
    .bytes 00000000000000000000000000000000                     ; 14186f263  ................
    .bytes 00000000000000000000000000000000                     ; 14186f273  ................
    .bytes 00000000000000000000000000000000                     ; 14186f283  ................
    .bytes 00000000000000000000000000000000                     ; 14186f293  ................
    .bytes 00000000000000000000000000000000                     ; 14186f2a3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f2b3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f2c3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f2d3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f2e3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f2f3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f303  ................
    .bytes 00000000000000000000000000000000                     ; 14186f313  ................
    .bytes 00000000000000000000000000000000                     ; 14186f323  ................
    .bytes 00000000000000000000000000000000                     ; 14186f333  ................
    .bytes 00000000000000000000000000000000                     ; 14186f343  ................
    .bytes 00000000000000000000000000000000                     ; 14186f353  ................
    .bytes 00000000000000000000000000000000                     ; 14186f363  ................
    .bytes 00000000000000000000000000000000                     ; 14186f373  ................
    .bytes 00000000000000000000000000000000                     ; 14186f383  ................
    .bytes 00000000000000000000000000000000                     ; 14186f393  ................
    .bytes 00000000000000000000000000000000                     ; 14186f3a3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f3b3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f3c3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f3d3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f3e3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f3f3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f403  ................
    .bytes 00000000000000000000000000000000                     ; 14186f413  ................
    .bytes 00000000000000000000000000000000                     ; 14186f423  ................
    .bytes 00000000000000000000000000000000                     ; 14186f433  ................
    .bytes 00000000000000000000000000000000                     ; 14186f443  ................
    .bytes 00000000000000000000000000000000                     ; 14186f453  ................
    .bytes 00000000000000000000000000000000                     ; 14186f463  ................
    .bytes 00000000000000000000000000000000                     ; 14186f473  ................
    .bytes 00000000000000000000000000000000                     ; 14186f483  ................
    .bytes 00000000000000000000000000000000                     ; 14186f493  ................
    .bytes 00000000000000000000000000000000                     ; 14186f4a3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f4b3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f4c3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f4d3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f4e3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f4f3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f503  ................
    .bytes 00000000000000000000000000000000                     ; 14186f513  ................
    .bytes 00000000000000000000000000000000                     ; 14186f523  ................
    .bytes 00000000000000000000000000000000                     ; 14186f533  ................
    .bytes 00000000000000000000000000000000                     ; 14186f543  ................
    .bytes 00000000000000000000000000000000                     ; 14186f553  ................
    .bytes 00000000000000000000000000000000                     ; 14186f563  ................
    .bytes 00000000000000000000000000000000                     ; 14186f573  ................
    .bytes 00000000000000000000000000000000                     ; 14186f583  ................
    .bytes 00000000000000000000000000000000                     ; 14186f593  ................
    .bytes 00000000000000000000000000000000                     ; 14186f5a3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f5b3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f5c3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f5d3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f5e3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f5f3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f603  ................
    .bytes 00000000000000000000000000000000                     ; 14186f613  ................
    .bytes 00000000000000000000000000000000                     ; 14186f623  ................
    .bytes 00000000000000000000000000000000                     ; 14186f633  ................
    .bytes 00000000000000000000000000000000                     ; 14186f643  ................
    .bytes 00000000000000000000000000000000                     ; 14186f653  ................
    .bytes 00000000000000000000000000000000                     ; 14186f663  ................
    .bytes 00000000000000000000000000000000                     ; 14186f673  ................
    .bytes 00000000000000000000000000000000                     ; 14186f683  ................
    .bytes 00000000000000000000000000000000                     ; 14186f693  ................
    .bytes 00000000000000000000000000000000                     ; 14186f6a3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f6b3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f6c3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f6d3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f6e3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f6f3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f703  ................
    .bytes 00000000000000000000000000000000                     ; 14186f713  ................
    .bytes 00000000000000000000000000000000                     ; 14186f723  ................
    .bytes 00000000000000000000000000000000                     ; 14186f733  ................
    .bytes 00000000000000000000000000000000                     ; 14186f743  ................
    .bytes 00000000000000000000000000000000                     ; 14186f753  ................
    .bytes 00000000000000000000000000000000                     ; 14186f763  ................
    .bytes 00000000000000000000000000000000                     ; 14186f773  ................
    .bytes 00000000000000000000000000000000                     ; 14186f783  ................
    .bytes 00000000000000000000000000000000                     ; 14186f793  ................
    .bytes 00000000000000000000000000000000                     ; 14186f7a3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f7b3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f7c3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f7d3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f7e3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f7f3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f803  ................
    .bytes 00000000000000000000000000000000                     ; 14186f813  ................
    .bytes 00000000000000000000000000000000                     ; 14186f823  ................
    .bytes 00000000000000000000000000000000                     ; 14186f833  ................
    .bytes 00000000000000000000000000000000                     ; 14186f843  ................
    .bytes 00000000000000000000000000000000                     ; 14186f853  ................
    .bytes 00000000000000000000000000000000                     ; 14186f863  ................
    .bytes 00000000000000000000000000000000                     ; 14186f873  ................
    .bytes 00000000000000000000000000000000                     ; 14186f883  ................
    .bytes 00000000000000000000000000000000                     ; 14186f893  ................
    .bytes 00000000000000000000000000000000                     ; 14186f8a3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f8b3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f8c3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f8d3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f8e3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f8f3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f903  ................
    .bytes 00000000000000000000000000000000                     ; 14186f913  ................
    .bytes 00000000000000000000000000000000                     ; 14186f923  ................
    .bytes 00000000000000000000000000000000                     ; 14186f933  ................
    .bytes 00000000000000000000000000000000                     ; 14186f943  ................
    .bytes 00000000000000000000000000000000                     ; 14186f953  ................
    .bytes 00000000000000000000000000000000                     ; 14186f963  ................
    .bytes 00000000000000000000000000000000                     ; 14186f973  ................
    .bytes 00000000000000000000000000000000                     ; 14186f983  ................
    .bytes 00000000000000000000000000000000                     ; 14186f993  ................
    .bytes 00000000000000000000000000000000                     ; 14186f9a3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f9b3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f9c3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f9d3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f9e3  ................
    .bytes 00000000000000000000000000000000                     ; 14186f9f3  ................
    .bytes 00000000000000000000000000000000                     ; 14186fa03  ................
    .bytes 00000000000000000000000000000000                     ; 14186fa13  ................
    .bytes 00000000000000000000000000000000                     ; 14186fa23  ................
    .bytes 00000000000000000000000000000000                     ; 14186fa33  ................
    .bytes 00000000000000000000000000000000                     ; 14186fa43  ................
    .bytes 00000000000000000000000000000000                     ; 14186fa53  ................
    .bytes 00000000000000000000000000000000                     ; 14186fa63  ................
    .bytes 00000000000000000000000000000000                     ; 14186fa73  ................
    .bytes 00000000000000000000000000000000                     ; 14186fa83  ................
    .bytes 00000000000000000000000000000000                     ; 14186fa93  ................
    .bytes 00000000000000000000000000000000                     ; 14186faa3  ................
    .bytes 00000000000000000000000000000000                     ; 14186fab3  ................
    .bytes 00000000000000000000000000000000                     ; 14186fac3  ................
    .bytes 00000000000000000000000000000000                     ; 14186fad3  ................
    .bytes 00000000000000000000000000000000                     ; 14186fae3  ................
    .bytes 00000000000000000000000000000000                     ; 14186faf3  ................
    .bytes 00000000000000000000000000000000                     ; 14186fb03  ................
    .bytes 00000000000000000000000000000000                     ; 14186fb13  ................
    .bytes 00000000000000000000000000000000                     ; 14186fb23  ................
    .bytes 00000000000000000000000000000000                     ; 14186fb33  ................
    .bytes 00000000000000000000000000000000                     ; 14186fb43  ................
    .bytes 00000000000000000000000000000000                     ; 14186fb53  ................
    .bytes 00000000000000000000000000000000                     ; 14186fb63  ................
    .bytes 00000000000000000000000000000000                     ; 14186fb73  ................
    .bytes 00000000000000000000000000000000                     ; 14186fb83  ................
    .bytes 00000000000000000000000000000000                     ; 14186fb93  ................
    .bytes 00000000000000000000000000000000                     ; 14186fba3  ................
    .bytes 00000000000000000000000000000000                     ; 14186fbb3  ................
    .bytes 00000000000000000000000000000000                     ; 14186fbc3  ................
    .bytes 00000000000000000000000000000000                     ; 14186fbd3  ................
    .bytes 00000000000000000000000000000000                     ; 14186fbe3  ................
    .bytes 00000000000000000000000000000000                     ; 14186fbf3  ................
    .bytes 00000000000000000000000000000000                     ; 14186fc03  ................
    .bytes 00000000000000000000000000000000                     ; 14186fc13  ................
    .bytes 00000000000000000000000000000000                     ; 14186fc23  ................
    .bytes 00000000000000000000000000000000                     ; 14186fc33  ................
    .bytes 00000000000000000000000000000000                     ; 14186fc43  ................
    .bytes 00000000000000000000000000000000                     ; 14186fc53  ................
    .bytes 00000000000000000000000000000000                     ; 14186fc63  ................
    .bytes 00000000000000000000000000000000                     ; 14186fc73  ................
    .bytes 00000000000000000000000000000000                     ; 14186fc83  ................
    .bytes 00000000000000000000000000000000                     ; 14186fc93  ................
    .bytes 00000000000000000000000000000000                     ; 14186fca3  ................
    .bytes 00000000000000000000000000000000                     ; 14186fcb3  ................
    .bytes 00000000000000000000000000000000                     ; 14186fcc3  ................
    .bytes 00000000000000000000000000000000                     ; 14186fcd3  ................
    .bytes 00000000000000000000000000000000                     ; 14186fce3  ................
    .bytes 00000000000000000000000000000000                     ; 14186fcf3  ................
    .bytes 00000000000000000000000000000000                     ; 14186fd03  ................
    .bytes 00000000000000000000000000000000                     ; 14186fd13  ................
    .bytes 00000000000000000000000000000000                     ; 14186fd23  ................
    .bytes 00000000000000000000000000000000                     ; 14186fd33  ................
    .bytes 00000000000000000000000000000000                     ; 14186fd43  ................
    .bytes 00000000000000000000000000000000                     ; 14186fd53  ................
    .bytes 00000000000000000000000000000000                     ; 14186fd63  ................
    .bytes 00000000000000000000000000000000                     ; 14186fd73  ................
    .bytes 00000000000000000000000000000000                     ; 14186fd83  ................
    .bytes 00000000000000000000000000000000                     ; 14186fd93  ................
    .bytes 00000000000000000000000000000000                     ; 14186fda3  ................
    .bytes 00000000000000000000000000000000                     ; 14186fdb3  ................
    .bytes 00000000000000000000000000000000                     ; 14186fdc3  ................
    .bytes 00000000000000000000000000000000                     ; 14186fdd3  ................
    .bytes 00000000000000000000000000000000                     ; 14186fde3  ................
    .bytes 00000000000000000000000000000000                     ; 14186fdf3  ................
    .bytes 00000000000000000000000000000000                     ; 14186fe03  ................
    .bytes 00000000000000000000000000000000                     ; 14186fe13  ................
    .bytes 00000000000000000000000000000000                     ; 14186fe23  ................
    .bytes 00000000000000000000000000000000                     ; 14186fe33  ................
    .bytes 00000000000000000000000000000000                     ; 14186fe43  ................
    .bytes 00000000000000000000000000000000                     ; 14186fe53  ................
    .bytes 00000000000000000000000000000000                     ; 14186fe63  ................
    .bytes 00000000000000000000000000000000                     ; 14186fe73  ................
    .bytes 00000000000000000000000000000000                     ; 14186fe83  ................
    .bytes 00000000000000000000000000000000                     ; 14186fe93  ................
    .bytes 00000000000000000000000000000000                     ; 14186fea3  ................
    .bytes 00000000000000000000000000000000                     ; 14186feb3  ................
    .bytes 00000000000000000000000000000000                     ; 14186fec3  ................
    .bytes 00000000000000000000000000000000                     ; 14186fed3  ................
    .bytes 00000000000000000000000000000000                     ; 14186fee3  ................
    .bytes 00000000000000000000000000000000                     ; 14186fef3  ................
    .bytes 00000000000000000000000000000000                     ; 14186ff03  ................
    .bytes 00000000000000000000000000000000                     ; 14186ff13  ................
    .bytes 00000000000000000000000000000000                     ; 14186ff23  ................
    .bytes 00000000000000000000000000000000                     ; 14186ff33  ................
    .bytes 00000000000000000000000000000000                     ; 14186ff43  ................
    .bytes 00000000000000000000000000000000                     ; 14186ff53  ................
    .bytes 00000000000000000000000000000000                     ; 14186ff63  ................
    .bytes 00000000000000000000000000000000                     ; 14186ff73  ................
    .bytes 00000000000000000000000000000000                     ; 14186ff83  ................
    .bytes 00000000000000000000000000000000                     ; 14186ff93  ................
    .bytes 00000000000000000000000000000000                     ; 14186ffa3  ................
    .bytes 00000000000000000000000000000000                     ; 14186ffb3  ................
    .bytes 00000000000000000000000000000000                     ; 14186ffc3  ................
    .bytes 00000000000000000000000000000000                     ; 14186ffd3  ................
    .bytes 00000000000000000000000000000000                     ; 14186ffe3  ................
    .bytes 00000000000000000000000000000000                     ; 14186fff3  ................
    .bytes 00000000000000000000000000000000                     ; 141870003  ................
    .bytes 00000000000000000000000000000000                     ; 141870013  ................
    .bytes 00000000000000000000000000000000                     ; 141870023  ................
    .bytes 00000000000000000000000000000000                     ; 141870033  ................
    .bytes 00000000000000000000000000000000                     ; 141870043  ................
    .bytes 00000000000000000000000000000000                     ; 141870053  ................
    .bytes 00000000000000000000000000000000                     ; 141870063  ................
    .bytes 00000000000000000000000000000000                     ; 141870073  ................
    .bytes 00000000000000000000000000000000                     ; 141870083  ................
    .bytes 00000000000000000000000000000000                     ; 141870093  ................
    .bytes 00000000000000000000000000000000                     ; 1418700a3  ................
    .bytes 00000000000000000000000000000000                     ; 1418700b3  ................
    .bytes 00000000000000000000000000000000                     ; 1418700c3  ................
    .bytes 00000000000000000000000000000000                     ; 1418700d3  ................
    .bytes 00000000000000000000000000000000                     ; 1418700e3  ................
    .bytes 00000000000000000000000000000000                     ; 1418700f3  ................
    .bytes 00000000000000000000000000000000                     ; 141870103  ................
    .bytes 00000000000000000000000000000000                     ; 141870113  ................
    .bytes 00000000000000000000000000000000                     ; 141870123  ................
    .bytes 00000000000000000000000000000000                     ; 141870133  ................
    .bytes 00000000000000000000000000000000                     ; 141870143  ................
    .bytes 00000000000000000000000000000000                     ; 141870153  ................
    .bytes 00000000000000000000000000000000                     ; 141870163  ................
    .bytes 00000000000000000000000000000000                     ; 141870173  ................
    .bytes 00000000000000000000000000000000                     ; 141870183  ................
    .bytes 00000000000000000000000000000000                     ; 141870193  ................
    .bytes 00000000000000000000000000000000                     ; 1418701a3  ................
    .bytes 00000000000000000000000000000000                     ; 1418701b3  ................
    .bytes 00000000000000000000000000000000                     ; 1418701c3  ................
    .bytes 00000000000000000000000000000000                     ; 1418701d3  ................
    .bytes 00000000000000000000000000000000                     ; 1418701e3  ................
    .bytes 00000000000000000000000000000000                     ; 1418701f3  ................
    .bytes 00000000000000000000000000000000                     ; 141870203  ................
    .bytes 00000000000000000000000000000000                     ; 141870213  ................
    .bytes 00000000000000000000000000000000                     ; 141870223  ................
    .bytes 00000000000000000000000000000000                     ; 141870233  ................
    .bytes 00000000000000000000000000000000                     ; 141870243  ................
    .bytes 00000000000000000000000000000000                     ; 141870253  ................
    .bytes 00000000000000000000000000000000                     ; 141870263  ................
    .bytes 00000000000000000000000000000000                     ; 141870273  ................
    .bytes 00000000000000000000000000000000                     ; 141870283  ................
    .bytes 00000000000000000000000000000000                     ; 141870293  ................
    .bytes 00000000000000000000000000000000                     ; 1418702a3  ................
    .bytes 00000000000000000000000000000000                     ; 1418702b3  ................
    .bytes 00000000000000000000000000000000                     ; 1418702c3  ................
    .bytes 00000000000000000000000000000000                     ; 1418702d3  ................
    .bytes 00000000000000000000000000000000                     ; 1418702e3  ................
    .bytes 00000000000000000000000000000000                     ; 1418702f3  ................
    .bytes 00000000000000000000000000000000                     ; 141870303  ................
    .bytes 00000000000000000000000000000000                     ; 141870313  ................
    .bytes 00000000000000000000000000000000                     ; 141870323  ................
    .bytes 00000000000000000000000000000000                     ; 141870333  ................
    .bytes 00000000000000000000000000000000                     ; 141870343  ................
    .bytes 00000000000000000000000000000000                     ; 141870353  ................
    .bytes 00000000000000000000000000000000                     ; 141870363  ................
    .bytes 00000000000000000000000000000000                     ; 141870373  ................
    .bytes 00000000000000000000000000000000                     ; 141870383  ................
    .bytes 00000000000000000000000000000000                     ; 141870393  ................
    .bytes 00000000000000000000000000000000                     ; 1418703a3  ................
    .bytes 00000000000000000000000000000000                     ; 1418703b3  ................
    .bytes 00000000000000000000000000000000                     ; 1418703c3  ................
    .bytes 00000000000000000000000000000000                     ; 1418703d3  ................
    .bytes 00000000000000000000000000000000                     ; 1418703e3  ................
    .bytes 00000000000000000000000000000000                     ; 1418703f3  ................
    .bytes 00000000000000000000000000000000                     ; 141870403  ................
    .bytes 00000000000000000000000000000000                     ; 141870413  ................
    .bytes 00000000000000000000000000000000                     ; 141870423  ................
    .bytes 00000000000000000000000000000000                     ; 141870433  ................
    .bytes 00000000000000000000000000000000                     ; 141870443  ................
    .bytes 00000000000000000000000000000000                     ; 141870453  ................
    .bytes 00000000000000000000000000000000                     ; 141870463  ................
    .bytes 00000000000000000000000000000000                     ; 141870473  ................
    .bytes 00000000000000000000000000000000                     ; 141870483  ................
    .bytes 00000000000000000000000000000000                     ; 141870493  ................
    .bytes 00000000000000000000000000000000                     ; 1418704a3  ................
    .bytes 00000000000000000000000000000000                     ; 1418704b3  ................
    .bytes 00000000000000000000000000000000                     ; 1418704c3  ................
    .bytes 00000000000000000000000000000000                     ; 1418704d3  ................
    .bytes 00000000000000000000000000000000                     ; 1418704e3  ................
    .bytes 00000000000000000000000000000000                     ; 1418704f3  ................
    .bytes 00000000000000000000000000000000                     ; 141870503  ................
    .bytes 00000000000000000000000000000000                     ; 141870513  ................
    .bytes 00000000000000000000000000000000                     ; 141870523  ................
    .bytes 00000000000000000000000000000000                     ; 141870533  ................
    .bytes 00000000000000000000000000000000                     ; 141870543  ................
    .bytes 00000000000000000000000000000000                     ; 141870553  ................
    .bytes 00000000000000000000000000000000                     ; 141870563  ................
    .bytes 00000000000000000000000000000000                     ; 141870573  ................
    .bytes 00000000000000000000000000000000                     ; 141870583  ................
    .bytes 00000000000000000000000000000000                     ; 141870593  ................
    .bytes 00000000000000000000000000000000                     ; 1418705a3  ................
    .bytes 00000000000000000000000000000000                     ; 1418705b3  ................
    .bytes 00000000000000000000000000000000                     ; 1418705c3  ................
    .bytes 00000000000000000000000000000000                     ; 1418705d3  ................
    .bytes 00000000000000000000000000000000                     ; 1418705e3  ................
    .bytes 00000000000000000000000000000000                     ; 1418705f3  ................
    .bytes 00000000000000000000000000000000                     ; 141870603  ................
    .bytes 00000000000000000000000000000000                     ; 141870613  ................
    .bytes 00000000000000000000000000000000                     ; 141870623  ................
    .bytes 00000000000000000000000000000000                     ; 141870633  ................
    .bytes 00000000000000000000000000000000                     ; 141870643  ................
    .bytes 00000000000000000000000000000000                     ; 141870653  ................
    .bytes 00000000000000000000000000000000                     ; 141870663  ................
    .bytes 00000000000000000000000000000000                     ; 141870673  ................
    .bytes 00000000000000000000000000000000                     ; 141870683  ................
    .bytes 00000000000000000000000000000000                     ; 141870693  ................
    .bytes 00000000000000000000000000000000                     ; 1418706a3  ................
    .bytes 00000000000000000000000000000000                     ; 1418706b3  ................
    .bytes 00000000000000000000000000000000                     ; 1418706c3  ................
    .bytes 00000000000000000000000000000000                     ; 1418706d3  ................
    .bytes 00000000000000000000000000000000                     ; 1418706e3  ................
    .bytes 00000000000000000000000000000000                     ; 1418706f3  ................
    .bytes 00000000000000000000000000000000                     ; 141870703  ................
    .bytes 00000000000000000000000000000000                     ; 141870713  ................
    .bytes 00000000000000000000000000000000                     ; 141870723  ................
    .bytes 00000000000000000000000000000000                     ; 141870733  ................
    .bytes 00000000000000000000000000000000                     ; 141870743  ................
    .bytes 00000000000000000000000000000000                     ; 141870753  ................
    .bytes 00000000000000000000000000000000                     ; 141870763  ................
    .bytes 00000000000000000000000000000000                     ; 141870773  ................
    .bytes 00000000000000000000000000000000                     ; 141870783  ................
    .bytes 00000000000000000000000000000000                     ; 141870793  ................
    .bytes 00000000000000000000000000000000                     ; 1418707a3  ................
    .bytes 00000000000000000000000000000000                     ; 1418707b3  ................
    .bytes 00000000000000000000000000000000                     ; 1418707c3  ................
    .bytes 00000000000000000000000000000000                     ; 1418707d3  ................
    .bytes 00000000000000000000000000000000                     ; 1418707e3  ................
    .bytes 00000000000000000000000000000000                     ; 1418707f3  ................
    .bytes 00000000000000000000000000000000                     ; 141870803  ................
    .bytes 00000000000000000000000000000000                     ; 141870813  ................
    .bytes 00000000000000000000000000000000                     ; 141870823  ................
    .bytes 00000000000000000000000000000000                     ; 141870833  ................
    .bytes 00000000000000000000000000000000                     ; 141870843  ................
    .bytes 00000000000000000000000000000000                     ; 141870853  ................
    .bytes 00000000000000000000000000000000                     ; 141870863  ................
    .bytes 00000000000000000000000000000000                     ; 141870873  ................
    .bytes 00000000000000000000000000000000                     ; 141870883  ................
    .bytes 00000000000000000000000000000000                     ; 141870893  ................
    .bytes 00000000000000000000000000000000                     ; 1418708a3  ................
    .bytes 00000000000000000000000000000000                     ; 1418708b3  ................
    .bytes 00000000000000000000000000000000                     ; 1418708c3  ................
    .bytes 00000000000000000000000000000000                     ; 1418708d3  ................
    .bytes 00000000000000000000000000000000                     ; 1418708e3  ................
    .bytes 00000000000000000000000000000000                     ; 1418708f3  ................
    .bytes 00000000000000000000000000000000                     ; 141870903  ................
    .bytes 00000000000000000000000000000000                     ; 141870913  ................
    .bytes 00000000000000000000000000000000                     ; 141870923  ................
    .bytes 00000000000000000000000000000000                     ; 141870933  ................
    .bytes 00000000000000000000000000000000                     ; 141870943  ................
    .bytes 00000000000000000000000000000000                     ; 141870953  ................
    .bytes 00000000000000000000000000000000                     ; 141870963  ................
    .bytes 00000000000000000000000000000000                     ; 141870973  ................
    .bytes 00000000000000000000000000000000                     ; 141870983  ................
    .bytes 00000000000000000000000000000000                     ; 141870993  ................
    .bytes 00000000000000000000000000000000                     ; 1418709a3  ................
    .bytes 00000000000000000000000000000000                     ; 1418709b3  ................
    .bytes 00000000000000000000000000000000                     ; 1418709c3  ................
    .bytes 00000000000000000000000000000000                     ; 1418709d3  ................
    .bytes 00000000000000000000000000000000                     ; 1418709e3  ................
    .bytes 00000000000000000000000000000000                     ; 1418709f3  ................
    .bytes 00000000000000000000000000000000                     ; 141870a03  ................
    .bytes 00000000000000000000000000000000                     ; 141870a13  ................
    .bytes 00000000000000000000000000000000                     ; 141870a23  ................
    .bytes 00000000000000000000000000000000                     ; 141870a33  ................
    .bytes 00000000000000000000000000000000                     ; 141870a43  ................
    .bytes 00000000000000000000000000000000                     ; 141870a53  ................
    .bytes 00000000000000000000000000000000                     ; 141870a63  ................
    .bytes 00000000000000000000000000000000                     ; 141870a73  ................
    .bytes 00000000000000000000000000000000                     ; 141870a83  ................
    .bytes 00000000000000000000000000000000                     ; 141870a93  ................
    .bytes 00000000000000000000000000000000                     ; 141870aa3  ................
    .bytes 00000000000000000000000000000000                     ; 141870ab3  ................
    .bytes 00000000000000000000000000000000                     ; 141870ac3  ................
    .bytes 00000000000000000000000000000000                     ; 141870ad3  ................
    .bytes 00000000000000000000000000000000                     ; 141870ae3  ................
    .bytes 00000000000000000000000000000000                     ; 141870af3  ................
    .bytes 00000000000000000000000000000000                     ; 141870b03  ................
    .bytes 00000000000000000000000000000000                     ; 141870b13  ................
    .bytes 00000000000000000000000000000000                     ; 141870b23  ................
    .bytes 00000000000000000000000000000000                     ; 141870b33  ................
    .bytes 00000000000000000000000000000000                     ; 141870b43  ................
    .bytes 00000000000000000000000000000000                     ; 141870b53  ................
    .bytes 00000000000000000000000000000000                     ; 141870b63  ................
    .bytes 00000000000000000000000000000000                     ; 141870b73  ................
    .bytes 00000000000000000000000000000000                     ; 141870b83  ................
    .bytes 00000000000000000000000000000000                     ; 141870b93  ................
    .bytes 00000000000000000000000000000000                     ; 141870ba3  ................
    .bytes 00000000000000000000000000000000                     ; 141870bb3  ................
    .bytes 00000000000000000000000000000000                     ; 141870bc3  ................
    .bytes 00000000000000000000000000000000                     ; 141870bd3  ................
    .bytes 00000000000000000000000000000000                     ; 141870be3  ................
    .bytes 00000000000000000000000000000000                     ; 141870bf3  ................
    .bytes 00000000000000000000000000000000                     ; 141870c03  ................
    .bytes 00000000000000000000000000000000                     ; 141870c13  ................
    .bytes 00000000000000000000000000000000                     ; 141870c23  ................
    .bytes 00000000000000000000000000000000                     ; 141870c33  ................
    .bytes 00000000000000000000000000000000                     ; 141870c43  ................
    .bytes 00000000000000000000000000000000                     ; 141870c53  ................
    .bytes 00000000000000000000000000000000                     ; 141870c63  ................
    .bytes 00000000000000000000000000000000                     ; 141870c73  ................
    .bytes 00000000000000000000000000000000                     ; 141870c83  ................
    .bytes 00000000000000000000000000000000                     ; 141870c93  ................
    .bytes 00000000000000000000000000000000                     ; 141870ca3  ................
    .bytes 00000000000000000000000000000000                     ; 141870cb3  ................
    .bytes 00000000000000000000000000000000                     ; 141870cc3  ................
    .bytes 00000000000000000000000000000000                     ; 141870cd3  ................
    .bytes 00000000000000000000000000000000                     ; 141870ce3  ................
    .bytes 00000000000000000000000000000000                     ; 141870cf3  ................
    .bytes 00000000000000000000000000000000                     ; 141870d03  ................
    .bytes 00000000000000000000000000000000                     ; 141870d13  ................
    .bytes 00000000000000000000000000000000                     ; 141870d23  ................
    .bytes 00000000000000000000000000000000                     ; 141870d33  ................
    .bytes 00000000000000000000000000000000                     ; 141870d43  ................
    .bytes 00000000000000000000000000000000                     ; 141870d53  ................
    .bytes 00000000000000000000000000000000                     ; 141870d63  ................
    .bytes 00000000000000000000000000000000                     ; 141870d73  ................
    .bytes 00000000000000000000000000000000                     ; 141870d83  ................
    .bytes 00000000000000000000000000000000                     ; 141870d93  ................
    .bytes 00000000000000000000000000000000                     ; 141870da3  ................
    .bytes 00000000000000000000000000000000                     ; 141870db3  ................
    .bytes 00000000000000000000000000000000                     ; 141870dc3  ................
    .bytes 00000000000000000000000000000000                     ; 141870dd3  ................
    .bytes 00000000000000000000000000000000                     ; 141870de3  ................
    .bytes 00000000000000000000000000000000                     ; 141870df3  ................
    .bytes 00000000000000000000000000000000                     ; 141870e03  ................
    .bytes 00000000000000000000000000000000                     ; 141870e13  ................
    .bytes 00000000000000000000000000000000                     ; 141870e23  ................
    .bytes 00000000000000000000000000000000                     ; 141870e33  ................
    .bytes 00000000000000000000000000000000                     ; 141870e43  ................
    .bytes 00000000000000000000000000000000                     ; 141870e53  ................
    .bytes 00000000000000000000000000000000                     ; 141870e63  ................
    .bytes 00000000000000000000000000000000                     ; 141870e73  ................
    .bytes 00000000000000000000000000000000                     ; 141870e83  ................
    .bytes 00000000000000000000000000000000                     ; 141870e93  ................
    .bytes 00000000000000000000000000000000                     ; 141870ea3  ................
    .bytes 00000000000000000000000000000000                     ; 141870eb3  ................
    .bytes 00000000000000000000000000000000                     ; 141870ec3  ................
    .bytes 00000000000000000000000000000000                     ; 141870ed3  ................
    .bytes 00000000000000000000000000000000                     ; 141870ee3  ................
    .bytes 00000000000000000000000000000000                     ; 141870ef3  ................
    .bytes 00000000000000000000000000000000                     ; 141870f03  ................
    .bytes 00000000000000000000000000000000                     ; 141870f13  ................
    .bytes 00000000000000000000000000000000                     ; 141870f23  ................
    .bytes 00000000000000000000000000000000                     ; 141870f33  ................
    .bytes 00000000000000000000000000000000                     ; 141870f43  ................
    .bytes 00000000000000000000000000000000                     ; 141870f53  ................
    .bytes 00000000000000000000000000000000                     ; 141870f63  ................
    .bytes 00000000000000000000000000000000                     ; 141870f73  ................
    .bytes 00000000000000000000000000000000                     ; 141870f83  ................
    .bytes 00000000000000000000000000000000                     ; 141870f93  ................
    .bytes 00000000000000000000000000000000                     ; 141870fa3  ................
    .bytes 00000000000000000000000000000000                     ; 141870fb3  ................
    .bytes 00000000000000000000000000000000                     ; 141870fc3  ................
    .bytes 00000000000000000000000000000000                     ; 141870fd3  ................
    .bytes 00000000000000000000000000000000                     ; 141870fe3  ................
    .bytes 00000000000000000000000000                           ; 141870ff3  .............

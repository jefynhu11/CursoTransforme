package com.times.jogadores.times;

import java.util.List;

import com.times.jogadores.jogadores.Jogador;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.OneToMany;
import jakarta.persistence.Table;

@Entity
@Table(name="time")
public class Time {

	@Id
	@GeneratedValue(strategy = GenerationType.UUID)
	@Column(length=36)
	private String id;
	private String nome;
	private String cor;
	
	public Time() {
		
	}
	
	public Time(DadosCadastroTime dados) {
		this.nome = dados.nome();
		this.cor = dados.cor();
	}
	
	@OneToMany()
	@JoinColumn(name="time_id", insertable=false, updatable=false)
	private List<Jogador> jogador;
	
	public String getId() {
		return id;
	}
	
	public void setId(String id) {
		this.id = id;
	}
	
	public String getNome() {
		return nome;
	}
	
	public void setNome(String nome) {
		this.nome = nome;
	}
	
	public String getCor() {
		return cor;
	}
	
	public void setCor(String cor) {
		this.cor = cor;
	}

	public List<Jogador> getJogador() {
		return jogador;
	}

	public void setJogador(List<Jogador> jogador) {
		this.jogador = jogador;
	}
	
}